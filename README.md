# GPA Calculator
Calculate your GPA

## Files:
- `gpa.py`: Python script to calculate the GPA.
- `gpa_data.txt`: A text file containing course names, letter grades, and credits in the format:
  ```txt
  course_name  letter_grade  credit
  ```
- `Makefile`: Used for building and running the GPA calculator (for both Linux and Windows environments).

## Setup

### Linux/Mac:
- Install dependencies (if needed):
   ```bash
   sudo apt install python3
   ```


### Windows:
- Install dependencies (if needed):
   ```bash
   # try running powershell with admin privilege 
   choco install make
   ```

### Run the GPA calculation:
   ```bash
   # This command will automatically run the file with the txt 
   make
   # if this makes error, then `Makefile` probably doesn't have 
   # executable permission so run the following command
   chmod +x Makefile
   ```
## Example Usage:
The `gpa_data.txt` should look like:
```txt
CS552   C+  4
CS350   A-  4
CS103   A-  4
CS108   A-  4
CS412   A   4
...
```