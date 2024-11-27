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
-- Query 1 Solver: 
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