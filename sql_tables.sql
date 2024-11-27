-- ==========================================================================================================
-- SQL Tables For Part 2
-- ==========================================================================================================

-- .import /workspaces/Project-2-Library-Management-System/LMSDataset/Publisher.csv PUBLISHER --skip 1
-- PUBLISHER: Publisher_Name, Phone, Address
-- PUBLISHER Table Creator: Chime Nguyen
CREATE TABLE IF NOT EXISTS PUBLISHER (
    -- Attributes
    Publisher_Name VARCHAR(27) NOT NULL, -- The number 27 came from the longest name from the publisher in the DB
    Phone CHAR(12) NOT NULL, -- The number 12 came from the max length of the phone number (excluding extensions)
    Address VARCHAR(120) NOT NULL, -- This contains the address of the publisher

    -- Primary Key & Secondary Keys
    PRIMARY KEY (Publisher_Name) -- Publisher_Name is a primary key that connects PUBLISHER with BOOK
    -- Phone is NOT a unique number in this case as Publishers can have the same phone number under different names
);


-- .import /workspaces/Project-2-Library-Management-System/LMSDataset/Library_Branch.csv LIBRARY_BRANCH --skip 1
-- LIBRARY_BRANCH: Branch_Id, Branch_Name, Branch_Address
-- LIBRARY_BRANCH Table Creator: Chime Nguyen
CREATE TABLE IF NOT EXISTS LIBRARY_BRANCH (
    -- Attributes
    Branch_Id INTEGER PRIMARY KEY NOT NULL, -- Branch_Id is a primary key that connects to BOOK_LOANS and BOOK_COPIES
    Branch_Name VARCHAR(11) NOT NULL,
    Branch_Address VARCHAR(120) NOT NULL
);


-- .import /workspaces/Project-2-Library-Management-System/LMSDataset/Borrower.csv BORROWER --skip 1
-- BORROWER: Card_No, Name, Address, Phone
-- BORROWER Table Creator: Ivan Ko
CREATE TABLE IF NOT EXISTS BORROWER (
    -- Attributes
    Card_No INTEGER PRIMARY KEY NOT NULL, -- Uniquely defines library borrowers
    Name VARCHAR(64) NOT NULL,
    Address VARCHAR(120) NOT NULL,
    Phone CHAR(12) NOT NULL,

    -- Primary Key & Secondary Keys
    UNIQUE (Phone) -- Phone is a unique number that corresponds with the Publisher (Secondary Key)
);


-- .import /workspaces/Project-2-Library-Management-System/LMSDataset/Book.csv BOOK --skip 1
-- BOOK: Book_Id, Title, Publisher_name
-- BOOK Table Creator: Ivan Ko
CREATE TABLE IF NOT EXISTS BOOK (
    -- Attributes
    Book_Id INTEGER PRIMARY KEY NOT NULL, -- Uniquely defines Books in the library system
    Title VARCHAR (128) NOT NULL,
    Publisher_name VARCHAR(64) NOT NULL,

    -- Foreign Keys & Foreign Key Constraints
    FOREIGN KEY (Publisher_name) REFERENCES PUBLISHER (Publisher_Name)
);


-- .import /workspaces/Project-2-Library-Management-System/LMSDataset/Book_Loans.csv BOOK_LOANS --skip 1
-- BOOK_LOANS: Book_Id, Branch_Id, Card_No, Date_Out, Due_Date, Returned_date
-- BOOK_LOANS Table Creator: Chime Nguyen
CREATE TABLE IF NOT EXISTS BOOK_LOANS (
    -- Attributes
    Book_Id INTEGER NOT NULL,
    Branch_Id INTEGER NOT NULL,
    Card_No INTEGER NOT NULL,
    Date_Out TEXT NOT NULL, -- Dates in TEXT format has to follow the YYYY-MM-DD format for date functions to work
    Due_Date TEXT NOT NULL,
    Returned_date TEXT NOT NULL,

    -- Primary Key & Secondary Keys
    PRIMARY KEY (Book_Id, Branch_Id, Card_No), -- These three foreign keys make up the primary key

    -- Foreign Keys & Foreign Key Constraints
    FOREIGN KEY (Book_Id) REFERENCES BOOK (Book_Id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (Branch_Id) REFERENCES LIBRARY_BRANCH (Branch_Id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (Card_No) REFERENCES BORROWER (Card_No) ON UPDATE CASCADE ON DELETE CASCADE
);


-- .import /workspaces/Project-2-Library-Management-System/LMSDataset/Book_Copies.csv BOOK_COPIES --skip 1
-- BOOK_COPIES: Book_Id, Branch_Id, No_Of_Copies
-- BOOK_COPIES Table Creator: Trung Nguyen
CREATE TABLE IF NOT EXISTS BOOK_COPIES (
    -- Attributes
    Book_Id INTEGER NOT NULL,
    Branch_Id INTEGER NOT NULL,
    No_Of_Copies INT NOT NULL,
    
    -- Primary Key & Secondary Keys
    PRIMARY KEY (Book_Id, Branch_Id), -- Combine these to get unique Book-Branch combo

    -- Foreign Keys & Foreign Key Constraints
    FOREIGN KEY (Book_Id) REFERENCES BOOK (Book_Id) ON UPDATE CASCADE ON DELETE CASCADE, -- Match Book_Id from Book
    FOREIGN KEY (Branch_Id) REFERENCES LIBRARY_BRANCH (Branch_Id) ON UPDATE CASCADE ON DELETE CASCADE -- Match Branch-Id from Library_Branch
);

--  .import /workspaces/Project-2-Library-Management-System/LMSDataset/Book_Authors.csv BOOK_AUTHORS --skip 1
-- BOOK_AUTHORS: Book_Id, Author_Name
-- BOOK_AUTHORS Table Creator: Trung Nguyen
CREATE TABLE IF NOT EXISTS BOOK_AUTHORS (
    -- Attributes
    Book_Id INTEGER NOT NULL,
    Author_Name VARCHAR(30), -- Arbitrary 30 value

    -- Primary Key & Secondary Keys
    PRIMARY KEY (Book_Id, Author_Name), -- Combine these to get unique (non-duplicate) book-authors

    -- Foreign Keys & Foreign Key Constraints
    FOREIGN KEY (Book_Id) REFERENCES BOOK(Book_Id) ON UPDATE CASCADE ON DELETE CASCADE -- Match Book_Id from Book
);


