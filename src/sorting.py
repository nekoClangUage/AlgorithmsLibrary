class BubbleSort:
    @staticmethod
    def simpleBubble(array):
        """Sorts a collection using the bubble sort algorithm.

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
    def oddEvenBubble(array):
        pass
