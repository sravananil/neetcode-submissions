class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Create an output array of the same length as nums.
        # Initialize every position with 1 because 1 is the
        # identity value for multiplication.
        output = [1] * len(nums)

        # LEFT PRODUCT:
        # Stores the product of all elements BEFORE the current index.
        left = 1

        # Traverse the array from left to right.
        for i in range(len(nums)):

            # Store the product of elements to the left of index i.
            output[i] = left

            # Include the current element in the left product
            # so it can be used for the next index.
            left *= nums[i]

        # RIGHT PRODUCT:
        # Stores the product of all elements AFTER the current index.
        right = 1

        # Traverse the array backwards, from right to left.
        for i in range(len(nums) - 1, -1, -1):

            # Multiply the previously stored left product
            # by the product of elements to the right.
            # This gives the product of all elements except nums[i].
            output[i] *= right

            # Include the current element in the right product
            # so it can be used for the previous index.
            right *= nums[i]

        # Return the final array containing products except self.
        return output