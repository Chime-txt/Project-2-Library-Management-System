-- ==========================================================================================================
-- SQL Tables For Part 2
-- ==========================================================================================================

-- .import ./Project-2-Library-Management-System/LMSDataset/Publisher.csv PUBLISHER --skip 1
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



-- .import ./Project-2-Library-Management-System/LMSDataset/Library_Branch.csv LIBRARY_BRANCH --skip 1
-- LIBRARY_BRANCH: Branch_Id, Branch_Name, Branch_Address
-- LIBRARY_BRANCH Table Creator: Chime Nguyen
CREATE TABLE IF NOT EXISTS LIBRARY_BRANCH (
    -- Attributes
    Branch_Id INTEGER PRIMARY KEY NOT NULL, -- Branch_Id is a primary key that connects to BOOK_LOANS and BOOK_COPIES
    Branch_Name VARCHAR(11) NOT NULL,
    Branch_Address VARCHAR(120) NOT NULL
);



-- .import ./Project-2-Library-Management-System/LMSDataset/Borrower.csv BORROWER --skip 1
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



-- .import ./Project-2-Library-Management-System/LMSDataset/Book.csv BOOK --skip 1
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



-- .import ./Project-2-Library-Management-System/LMSDataset/Book_Loans.csv BOOK_LOANS --skip 1
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



-- .import ./Project-2-Library-Management-System/LMSDataset/Book_Copies.csv BOOK_COPIES --skip 1
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



--  .import ./Project-2-Library-Management-System/LMSDataset/Book_Authors.csv BOOK_AUTHORS --skip 1
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



-- ===========================================================================================================
-- SQL Queries For Part 2
-- ===========================================================================================================
-- SQL Query Templates
-- SELECT                   -- INSERT INTO              -- UPDATE 
-- FROM                     -- VALUES                   -- SET    
-- [WHERE]                                              -- [WHERE]
-- [GROUP BY [HAVING]]      -- DELETE FROM
-- [ORDER BY]               -- [WHERE]    
-- ===========================================================================================================
-- Aliases For The Tables
-- PUBLISHER p
-- LIBRARY_BRANCH lb
-- BORROWER bo
-- BOOK b
-- BOOK_LOANS bl
-- BOOK_COPIES bc
-- BOOK_AUTHOR ba
-- ===========================================================================================================

-- Question 1: Insert yourself as a New Borrower. Do not provide the Card_no in your query.
-- Question 1 Solver: Chime Nguyen
-- Borrower has Card_No, Name, Address, Phone, we will only be using the latter three attributes.
-- Since Card_No is a primary key, it will auto increment as necessary
INSERT INTO BORROWER (Name, Address, Phone)
VALUES ('Chime Nguyen','701 S Nedderman Dr, Texas, TX 76019', '211-211-2112');



-- Question 2: Update your phone number to (837) 721-8965
-- Question 2 Solver: Trung Nguyen
UPDATE BORROWER
SET Phone = '837-721-8965'   
WHERE Name = 'Chime Nguyen';



-- Assumption: Increase the number of copies for ALL books in the 'East Branch'
-- Question 3: Increase the number of book_copies by 1 for the 'East Branch'
-- Question 3 Solver: Trung Nguyen
UPDATE BOOK_COPIES
SET No_Of_Copies = No_Of_Copies + 1   
WHERE Branch_Id = (SELECT Branch_Id
                    FROM LIBRARY_BRANCH
                    WHERE Branch_Name = 'East Branch'
);
-- Could hard-code the id value of the 'East Branch" (3) instead of looking for it



-- Question 4-a: Insert a new BOOK with the following info: Title: 'Harry Potter and the Sorcerer's Stone' ; 
-- Book_author: 'J.K. Rowling' ; Publisher_name: 'Oxford Publisheing'
-- Question 4-a Solver: Trung Nguyen & Chime Nguyen
INSERT INTO PUBLISHER (Publisher_Name, Phone, Address) -- not sure if you need the phone and address
VALUES ('Oxford Publisheing', 'NULL', 'NULL'); -- would just be null, null anyways since it wasn't specified/given
INSERT INTO BOOK (Title, Publisher_name)
VALUES ('Harry Potter and the Sorcerer''s Stone', 'Oxford Publisheing');
INSERT INTO BOOK_AUTHORS (Book_Id, Author_Name)    
VALUES ((SELECT Book_Id FROM BOOK WHERE Title = 'Harry Potter and the Sorcerer''s Stone'), 'J.K. Rowling');
-- Not entirely sure about this one since we didn't explicitly give it a book_id value



-- Question 4-b: You also need to insert the following branches:
-- +------------+---------------------------------+
-- |North Branch|456 NW, Irving, TX 76100         |
-- +------------+---------------------------------+
-- |UTA Branch  |123 Cooper St, Arlington TX 76101|
-- +------------+---------------------------------+
-- Question 4-b Solver: Trung Nguyen
INSERT INTO LIBRARY_BRANCH (Branch_Name, Branch_Address)
VALUES ('North Branch', '456 NW, Irving, TX 76100');
INSERT INTO LIBRARY_BRANCH (Branch_Name, Branch_Address)
VALUES ('UTA Branch', '123 Cooper St, Arlington TX 76101');



-- Question 5: Return all Books that were loaned between March 5, 2022 until March 23, 2022. List Book 
-- title and Branch name, and how many days it was borrowed for.
-- Question 5 Solver: Trung Nguyen
-- Notes: JULIANDAY converts it into a date format you can do arithmetic on
--        Casted it as INTEGER because it'd return as a decimal .0
SELECT B.Title, LB.Branch_Name,
    CASE WHEN BL.Returned_date IS NOT 'NULL' THEN 
            CAST(JULIANDAY(BL.Returned_date) - JULIANDAY(BL.Date_Out) AS INTEGER)
        ELSE CAST(JULIANDAY(CURRENT_DATE) - JULIANDAY(BL.Date_Out) AS INTEGER) 
            -- Today's date meaning it was never returned 
    END AS Days_Borrowed
FROM BOOK_LOANS BL JOIN BOOK B ON BL.Book_Id = B.Book_Id
    JOIN LIBRARY_BRANCH LB ON BL.Branch_Id = LB.Branch_Id 
WHERE BL.Date_Out BETWEEN '2022-03-05' AND '2022-03-23'
ORDER BY B.Title, LB.Branch_Name;



-- Question 6: Return a List borrower names, that have books not returned.
-- Question 6 Solver: Chime Nguyen
-- Result:
-- +----------------+
-- | Borrower_Names |
-- +----------------+
-- | Jane Doe       |
-- | Bob Johnson    |
-- +----------------+
-- The DISTINCT keyword ensures that the same borrower does not show up more than once as they may have more
-- than one book that they haven't returned
SELECT DISTINCT bo.Name AS Borrower_Names
FROM BORROWER bo JOIN BOOK_LOANS bl ON bo.Card_No = bl.Card_No
WHERE Returned_date = 'NULL';     



-- Question 7: Create a report that will return all branches with the number of books borrowed per branch 
-- separated by if they have been returned, still borrowed, or late.
-- Question 7 Solver: Chime Nguyen
-- In this case, I am treating the returned column as books turned in on time or earlier, as late is
SELECT lb.Branch_Name,
    COUNT(*) AS Book_Count,
    COUNT(CASE WHEN bl.Returned_date IS NOT 'NULL' THEN 1 END) AS Returned_Books, 
    COUNT(CASE WHEN bl.Returned_date IS 'NULL' THEN 1 END) AS Still_Borrowed_Books, 
    COUNT(CASE WHEN bl.Returned_date IS NOT 'NULL' AND bl.Returned_date > bl.Due_Date THEN 1 END) AS Late_Books
FROM LIBRARY_BRANCH lb JOIN BOOK_LOANS bl ON lb.Branch_Id = bl.Branch_Id
GROUP BY lb.Branch_Name;



-- Question 8: List all the books (title) and the maximum number of days that they were borrowed.
-- Question 8 Solver: Ivan Ko
SELECT b.Title, MAX(CASE WHEN bl.Returned_date = 'NULL' THEN NULL
    ELSE CAST(JULIANDAY(bl.Returned_date) - JULIANDAY(bl.Date_Out) AS INTEGER) 
    END) AS Days_borrowed 
FROM BOOK b JOIN BOOK_LOANS bl ON b.Book_Id = bl.Book_Id
GROUP BY b.Book_Id
ORDER BY Days_borrowed DESC; -- Optional, but is included because it is easier to see the maximum number of days


-- Question 9: Create a report for Ethan Martinez with all the books they borrowed. List the book title and 
-- author. Also, calculate the number of days each book was borrowed for and if any book is late being 
-- returned. Order the results by the date_out.
-- Question 9 Solver: Ivan Ko & Trung Nguyen
SELECT bo.Name, b.Title, ba.Author_Name AS Author, bl.Date_Out, 
    CASE WHEN bl.Returned_date IS NOT 'NULL' THEN
        CAST(JULIANDAY(bl.Returned_date) - JULIANDAY(bl.Date_Out) AS INTEGER)
        ELSE 'NULL'
    END AS Days_borrowed,
    CASE
        WHEN bl.Returned_date IS 'NULL' THEN 'Not Returned'
        WHEN bl.Returned_date IS NOT 'NULL' AND JULIANDAY(bl.Returned_date) > JULIANDAY(bl.Due_Date)
        THEN 'Late' ELSE 'On Time'
    END AS Return_Status
FROM BOOK b JOIN BOOK_LOANS bl ON b.Book_Id = bl.Book_Id
            JOIN BORROWER bo ON bl.Card_No = bo.Card_No
            JOIN BOOK_AUTHORS ba ON b.Book_Id = ba.Book_Id
WHERE bo.Name = 'Ethan Martinez'
ORDER BY Date_Out DESC;


-- Question 10: Return the names of all borrowers that borrowed a book from the West Branch include their 
-- addresses.
-- Question 10 Solver: Ivan Ko
       
SELECT DISTINCT bo.Name, bo.Address, lb.Branch_Name
FROM BORROWER bo JOIN BOOK_LOANS bl ON bo.Card_No = bl.Card_No
                 JOIN LIBRARY_BRANCH lb ON bl.Branch_Id = lb.Branch_Id
WHERE lb.Branch_Name = 'West Branch';


-- ===========================================================================================================
-- SQL Queries For Part 3
-- ===========================================================================================================

-- Query 1:
-- Add an extra column 'Late' to the Book_Loan table. Values will be 0-for non-late retuns, and 1-for late 
-- returns. Then update the 'Late' column with '1' for all records that they have a return date later than the
-- due date and with '0' for those were returned on time.
-- Query 1 Solver: Ivan Ko
-- This query does not account for books that weren't turned in at all, so we should mark this column as
-- non-late

ALTER TABLE BOOK_LOANS ADD COLUMN Late INTEGER;

UPDATE BOOK_LOANS
SET Late = (
    CASE
        WHEN CAST(JULIANDAY(Returned_date) > JULIANDAY(Due_Date) AS INTEGER) THEN 1
        WHEN CAST(JULIANDAY(Returned_date) <= JULIANDAY(Due_Date) AS INTEGER) THEN 0
        ELSE 0
    END
    );


-- Query 2:
-- Add an extra column 'LateFee' to the Library_Branch table, decide late fee per day for each branch and 
-- update that column.
-- Query 2 Solver: Ivan Ko

ALTER TABLE LIBRARY_BRANCH ADD COLUMN LateFee FLOAT DEFAULT 0.00;

UPDATE LIBRARY_BRANCH
SET LateFee = (
    CASE
        WHEN Branch_Name = 'Main Branch' THEN 100.00
        WHEN Branch_Name = 'West Branch' THEN 50.00
        WHEN Branch_Name = 'East Branch' THEN 10.00
        ELSE 420.69
    END
    );

-- Query 3:
-- Create a view vBookLoanInfo that retrieves all information per book loan. The view should have the 
-- following attributes:  
--    • Card_No,  
--    • Borrower Name 
--    • Date_Out,  
--    • Due_Date,  
--    • Returned_date  
--    • Total Days of book loaned out as 'TotalDays'– you need to change weeks to days  
--    • Book Title 
--    • Number of days returned late – if returned before or on due_date place zero 
--    • Branch ID 
--    • Total Late Fee Balance 'LateFeeBalance' – If the book was not retuned late than fee = '0'
-- Query 3 Solver: Trung Nguyen
-- Trung is attemping this one 

CREATE VIEW vBookLoanInfo AS
SELECT 
    BL.Card_No,
    BR.Name AS 'Borrower Name',
    BL.Date_Out,
    BL.Due_Date,
    BL.Returned_date,
    CAST((JULIANDAY(BL.Returned_date) - JULIANDAY(BL.Date_Out)) AS INTEGER) AS TotalDays,
    B.Title AS 'Book Title',
    CASE WHEN BL.Late = 1 
        THEN CAST((JULIANDAY(BL.Returned_date) - JULIANDAY(BL.Due_Date)) AS INTEGER)
        ELSE 0 --Assumption that it's 0 days late rather than just NULL
    END AS 'Days Returned Late',
    BL.Branch_Id,
    CASE WHEN BL.Late = 1
        THEN CAST((JULIANDAY(BL.Returned_date) - JULIANDAY(BL.Due_Date)) AS INTEGER) * LB.LateFee
    END AS LateFeeBalance
From BOOK_LOANS BL
JOIN BORROWER BR ON BL.Card_No = BR.Card_No
JOIN BOOK B ON BL.BOOK_Id = B.Book_Id
JOIN LIBRARY_BRANCH LB ON BL.Branch_Id = LB.Branch_Id;
