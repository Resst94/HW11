# HW11
Tasks

- Add a field for birthday Birthday. This field is optional, but there can be only one.
- Add the functionality of working with Birthday to the Record class, namely the days_to_birthday function, which returns the number of days until the next birthday.
- Add functionality to check for the correctness of the values for the Phone, Birthday fields.
- Add pagination (page-by-page output) for AddressBook for situations when the book is very large and you need to show the contents in parts, not all at once. We implement this by creating an iterator by records.

Acceptance criteria:

- AddressBook implements the iterator method, which returns a generator by AddressBook records and returns a view for N records in one iteration.
- The Record class accepts one more additional (optional) argument of the Birthday class
- The Record class implements the days_to_birthday method, which returns the number of days until the contact's next birthday if the birthday is specified.
- setter and getter logic for the value attributes of Field's inheritors.
- Checking for the correctness of the slave phone number setter for the value of the Phone class.
- Checking for the correctness of the managed birthday setter for the value of the Birthday class.
