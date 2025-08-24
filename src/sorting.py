import multiprocessing as mpi 

def swap(array, i, j):
    """
        Swap elements in array

        Args:
            array: Any object that supports iteration, indexing, and whose
                         elements support comparison operations.
            i: index element in array.
            j: index element in array.
    """
    temp = array[j]

    array[j] = array[i]
    array[i] = temp

class BubbleSort:
    @staticmethod
    def simpleBubble(array):
        """
        Sorts a collection using the bubble sort algorithm.

        Args:
            array: Any object that supports iteration, indexing, and whose
                         elements support comparison operations.
        """
        i = 0
        arr_len = len(array)
        
        while(i < arr_len - 1):
            j = 0
            while(j < arr_len - i - 1):
                if(array[j] > array[j + 1]):
                    temp_val = array[j + 1]
                    array[j + 1] = array[j]
                    array[j] = temp_val

                j += 1
            i += 1

    @staticmethod
    def oddEvenBubble(array, num_processes=2):
        """
        Sorts a collection using a parallelized odd-even sort.

        Args:
            num_processes: The number of processes to use for sorting.
            array: Any object that supports iteration, indexing, and whose
                         elements support comparison operations.            
        """
        arr_len = len(array)
        if arr_len < 2:
            return

        if num_processes < 1 or num_processes > 20:
            num_processes = 1

        def pass_worker(shared_list, start_index, step):
            for j in range(start_index, arr_len, step):
                if shared_list[j] < shared_list[j - 1]:
                    swap(shared_list, j - 1, j)

        with mpi.Manager() as manager:
            shared_list = manager.list(array)
            processes = []
            step = 2 * num_processes

            for i in range(arr_len):
                processes.clear()
                start_offset = 1 if i % 2 == 0 else 2

                for j in range(num_processes):
                    start_index = start_offset + 2 * j
                    p = mpi.Process(target=pass_worker, args=(shared_list, start_index, step))
                    processes.append(p)
                    p.start()

                for p in processes:
                    p.join()

            for i in range(arr_len):
                array[i] = shared_list[i]

    @staticmethod
    def oddEvenBubbleSingleThread(array):
        """
        Sorts a collection using the bubble sort algorithm (single thread; no parallelism).
        Args:
            array: Any object that supports iteration, indexing, and whose
                        elements support comparison operations.
        """
        i = 0
        arr_len = len(array)
        while(i < arr_len):
            if(i % 2 == 0):        
                for j in range(2, arr_len, 2):
                    if(array[j] < array[j - 1]):
                        swap(array, j - 1, j)
            else:
                for j in range(1, arr_len, 2):
                    if(array[j] < array[j - 1]):
                        swap(array, j - 1, j)
            i += 1
