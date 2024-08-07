# ENSF 592 Term Project

## 📚 Learning Outcomes

- Design and document a terminal-based Python application
- Select, import, and manipulate a set of data
- Merge multiple datasets using Pandas
- Use hierarchical indexing to sort and slice data
- Process data according to user input
- Operate on data in Pandas and NumPy
- Display data using Matplotlib

## 💻 Program Specifications

For this final project, you have flexibility to design and develop your own terminal-based data analysis program in Python.
Your application must meet the following design specifications:

- Your final output should match the given examples (see attached screenshots)
- Stage 1: Dataset Selection
  - Several suggested datasets are included in the project repository. You may use the provide data or select datasets of your own choosing.
  - You must use at least three separate Excel sheets or files that can be related in some way.
  - Your final combined dataset (see next stage) must have at least ten columns and 200 rows.
  - You may edit the given datasets before you begin coding, but your program should not modify the Excel files directly.
  - You may not hard-code/copy-paste any information into your program except for the Excel column names.
- Stage 2: DataFrame Creation
  - Import your chosen data into a Pandas DataFrames.
  - You must use at least two merge/join operations and you must delete any duplicated columns/rows that result from the merge.
  - You must create a hierarchical index of at least two levels (row or column).
  - All data should be presented in the correctly sorted order, depending on the index.
  - You may not use global variables. You must import the data within your main function.
  - Remember to check for null values or data mismatches.
- Stage 3: User Entry
  - Your application must return useful information. Design an interface that allows users to search based on some sort of criteria or keywords.
  - The user must provide at least two pieces of information/selection (e.g. "school name" and "grade")
  - Give the user clear input instructions. If an invalid entry is given, use try/except statements to handle the error. Your program should not terminate.
  - You must not hard-code any data values (the data within your spreadsheets could be changed!).
  - Any output information must be clearly defined using printed headers.
- Stage 4: Analysis and Calculations
  - You may choose what data trends to presents from your data. However, you must meet the following specifications.
  - Use the describe method to print aggregate stats for the entire dataset.
  - Add at least two columns to the combined dataset.
  - Use an aggregation computation for a subset of the data.
  - Use a masking operation.
  - Use the groupby operation at least once.
  - Create and print a pivot table.
  - Include at least two user-defined functions or a class that contains two methods.
- Stage 5: Export and Matplotlib
  - Export your entire merged, hierarchical dataset to an Excel file in the working directory. Be sure to include the index and header values. The TAs will use this to verify the structure of your dataset.
  - Use your data to create at least one plot using Matplotlib. Save the plot as a `.png` file and upload to the repository.
- Your code must follow the conventions discussed so far in the course (names_with_underscores, ClassNames, four spaces for indentations, spaces between variables/operators, comments throughout, etc.)
- All classes, methods, and functions must contain docstring documentation.
  - For each class, include a functionality summary and describe any class and/or instance variables (do not include a separate docstring for \_\_init\_\_)
  - For each method/function, include a functionality summary and describe parameters and return values (or specify if there are none)
  - Main functions do not need a docstring but should be well-commented
- You may go beyond the minimum requirements specified here!
- Your code will be run by the TAs as your end user.
- FAQs about the project will be answered on the D2L discussion boards. Please check the boards for any clarifications before submitting.
- The grading rubric is included in this repository and posted to D2L.

## 📝 Assignment Tasks and Deliverables

- You must submit the following items within your repository (one repo per team if working with a partner):
  - Your Python code files
  - Screenshots of successful execution
  - Plot output as a `.png` file
  - Your input dataset
  - Your exported dataset
  - A brief PDF summary of how your project meets the requirements (include a citation for your dataset)
  - You do not need to create a new README file- your user input instructions should be clear from your interface, but you may put any introductory information directly in the comments under your code header.
  - You will also give a 5 minute presentation during the lab on June 17th. All team members must participate. Be prepared to answer questions about your program. If you are unable to attend the lab, you must make arrangements with Dr. Marasco ahead of the session. Presentations will be recorded for the TA/instructor to view only.
- Make sure to watch all video lessons and labs, and review the corresponding Jupyter Notebooks.
- Clone this repository to your local computer.
- Open VSCode and start a new terminal. Make sure that your `ensf592` environment is activated.
- Create your `.py` file and remember to place your information in the header.
- Remember to test your program execution via the terminal.
- Take a screenshot of your successful program run and upload it to your assignment repository.
- Commit your screenshot and code.
- Push your local git history to github: `git push origin main`
- One member of your team should submit your repository HTTPS link to the Project dropbox. Please list both members' names and your group number in the textbox.
- Tip: If you want to learn more about a specific aspect of a Python object or the functionality of imported modules, remember to take a look at the official documentation!
