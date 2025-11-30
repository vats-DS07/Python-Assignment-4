import numpy as num
def array (arr,name="Array"):
    print(name)
    print(f"Elements: {arr}")
    print(arr.shape)
    print(arr.ndim)
    print(arr.dtype)

def main():
    array1=num.array([1,2,3,4,5])
    array2=num.array([
        [1,2,3],
        [4,5,6],
    ])
    array(array1,"1D Array")
    array(array2,"2D Array")


if __name__=="__main__":
    main()