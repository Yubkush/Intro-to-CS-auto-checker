import subprocess
import os

TEST_OUTPUT = "out.txt"


def compare_text(file1, file2):
    """
    return if the contents of two text files are equal.
    """
    with open(file1, "r") as file1:
        lines1 = file1.readlines()
    with open(file2, "r") as file2:
        lines2 = file2.readlines()
    return lines1 == lines2


def test_file(input_path: str, input_file_name: str, output_path: str, exe_path: str):
    """
    runs an executable program that recieves input text file, and outputs text to an output text file,
    then checks if the output is correct according to the matching correct output.
    """
    with open(os.path.join(input_path, input_file_name), "r") as inputf:
        input_data = inputf.read()
    with open(os.path.join(output_path, TEST_OUTPUT), "w") as test_output_file:
        subprocess.run(
            [exe_path],
            shell=True,
            text=True,
            input=input_data,
            stdout=test_output_file,
        )
        test_num = input_file_name.split(".")[0][-1]
        # The first and only item in a list that contains only file names that match the input
        correct_output = [
            file
            for file in os.listdir(output_path)
            if file.split(".")[0][-1] == test_num
        ]
        # if list is not empty
        if correct_output:
            correct_output = correct_output[0]
            correct_output_path = os.path.join(output_path, correct_output)
            if compare_text(
                os.path.join(output_path, TEST_OUTPUT), correct_output_path
            ):
                print(f"test {test_num} passed")
            else:
                print(f"test {test_num} failed")


def tester():
    input_path = input("Enter input files path:")
    output_path = input("Enter output files path:")
    exe_path = input("Enter executable path:")
    with open(os.path.join(output_path, TEST_OUTPUT), "w") as test_output_file:
        input_files_list = os.listdir(input_path)
        for input_file_name in input_files_list:
            test_file(input_path, input_file_name, output_path, exe_path)
    os.remove(os.path.join(output_path, TEST_OUTPUT))


if __name__ == "__main__":
    tester()
