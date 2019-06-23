from scale_zip import ScaleZip

if __name__ == "__main__":
    user_input1 = int(input())
    user_input2 = int(input())
    filename = "example1.zip"
    ScaleZip(filename, user_input1, user_input2).process_zip()