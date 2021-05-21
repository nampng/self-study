# 1.7 Rotate Matrix
# Given an image represented by an N x N matrix, where each pixel in the image is
# represented by an integer, write a method to rotate the image by 90 degrees.
# Can you do this in place?

# Super uneligant. Must optimize and also find a way to do it in place.
def Rotate(image):
    array = []
    for i in image[-1]:
        array.append([i])
    
    for row in image[-2::-1]:
        for i in range(len(row)):
            array[i].append(row[i])
    
    print(array)

if __name__ == "__main__":
    arr1 = [[1,2,3], [4,5,6], [7,8,9]]
    Rotate(arr1)