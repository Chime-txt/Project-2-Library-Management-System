-- ==========================================================================================================
-- SQL Queries For Part 2
-- ==========================================================================================================
-- SQL Query Templates
-- SELECT                   -- INSERT INTO              -- UPDATE 
-- FROM                     -- VALUES                   -- SET    
-- [WHERE]                                              -- [WHERE]
-- [GROUP BY [HAVING]]      -- DELETE FROM
-- [ORDER BY]               -- [WHERE]    
-- ==========================================================================================================
-- Aliases For The Tables
-- PUBLISHER p
-- LIBRARY_BRANCH lb
-- BORROWER bo
-- BOOK b
-- BOOK_LOANS bl
-- BOOK_COPIES bc
-- BOOK_AUTHOR ba
-- ==========================================================================================================

-- Question 1: Insert yourself as a New Borrower. Do not provide the Card_no in your query.
-- Question 1 Solver: Chime Nguyen
-- Borrower has Card_No, Name, Address, Phone, we will only be using the latter three attributes.
-- Since Card_No is a primary key, it will auto increment as necessary
INSERT INTO BORROWER (Name, Address, Phone)
VALUES ('Chime Nguyen', '701 S Nedderman Dr, Texas, TX 76019', '211-211-2112');



-- Question 2: Update your phone number to (837) 721-8965
-- Question 2 Solver: 
-- UPDATE 
-- SET    
-- [WHERE]



-- Question 3: Increase the number of book_copies by 1 for the ‘East Branch’
-- Question 3 Solver: 
-- UPDATE 
-- SET    
-- [WHERE]



-- Question 4-a: Insert a new BOOK with the following info: Title: ‘Harry Potter and the Sorcerer's Stone’ ; 
-- Book_author: ‘J.K. Rowling’ ; Publisher_name: ‘Oxford Publisheing’
-- Question 4-a Solver: 
-- UPDATE 
-- SET    
-- [WHERE]



-- Question 4-b: You also need to insert the following branches:
-- +------------+---------------------------------+
-- |North Branch|456 NW, Irving, TX 76100         |
-- +------------+---------------------------------+
-- |UTA Branch  |123 Cooper St, Arlington TX 76101|
-- +------------+---------------------------------+
-- Question 4-b Solver: 
-- UPDATE 
-- SET    
-- [WHERE]



-- Question 5: Return all Books that were loaned between March 5, 2022 until March 23, 2022. List Book 
-- title and Branch name, and how many days it was borrowed for.
-- Question 5 Solver: 
-- SELECT             
-- FROM               
-- [WHERE]            
-- [GROUP BY [HAVING]]
-- [ORDER BY]         



-- Question 6: Return a List borrower names, that have books not returned.
-- Question 6 Solver: Chime Nguyen
-- The DISTINCT keyword ensures that the same borrower does not show up more than once as they may have more
-- than one book that they haven't returned
SELECT DISTINCT bo.Name AS Borrower_Names
FROM BORROWER bo JOIN BOOK_LOANS bl ON bo.Card_No = bl.Card_No
WHERE Returned_date = NULL;     



-- Question 7: Create a report that will return all branches with the number of books borrowed per branch 
-- separated by if they have been returned, still borrowed, or late.
-- Question 7 Solver: Chime Nguyen
-- In this case, I am treating the returned column as books turned in on time or earlier, as late is
SELECT lb.Branch_Name,
    -- Select the total number of books returned at any time on or before the due date (Version 1)
    (SELECT COUNT(*)
        FROM BOOK_LOANS
        WHERE Returned_date <= Due_Date
    ) AS Returned_Books_V1,

    -- Select the total number of books returned at all times (Version 2)
    (SELECT COUNT(*)
        FROM BOOK_LOANS
        WHERE Returned_date != NULL
    ) AS Returned_Books_V2,

    -- Select the total number of books still borrowed
    (SELECT COUNT(*)
        FROM BOOK_LOANS
        WHERE Returned_date = NULL
    ) AS Still_Borrowed_Books,

    -- Select the total number of books late
    (SELECT COUNT(*)
        FROM BOOK_LOANS
        WHERE Returned_date > Due_Date
    ) AS Late_Books

FROM LIBRARY_BRANCH lb JOIN BOOK_LOANS bl ON lb.Branch_Id = bl.Branch_Id
GROUP BY lb.Branch_Name, Returned_Books, Still_Borrowed_Books, Late_Books;



-- Question 8: List all the books (title) and the maximum number of days that they were borrowed.
-- Question 8 Solver: 
-- SELECT             
-- FROM               
-- [WHERE]            
-- [GROUP BY [HAVING]]
-- [ORDER BY]         



-- Question 9: Create a report for Ethan Martinez with all the books they borrowed. List the book title and 
-- author. Also, calculate the number of days each book was borrowed for and if any book is late being 
-- returned. Order the results by the date_out.
-- Question 9 Solver: 
-- SELECT             
-- FROM               
-- [WHERE]            
-- [GROUP BY [HAVING]]
-- [ORDER BY]         



-- Question 10: Return the names of all borrowers that borrowed a book from the West Branch include their 
-- addresses.
-- Question 10 Solver:
-- SELECT             
-- FROM               
-- [WHERE]            
-- [GROUP BY [HAVING]]
-- [ORDER BY]         



-- ==========================================================================================================
-- SQL Queries For Part 3
-- ==========================================================================================================

-- Query 1:
-- Add an extra column ‘Late’ to the Book_Loan table. Values will be 0-for non-late retuns, and 1-for late 
-- returns. Then update the ‘Late’ column with '1' for all records that they have a return date later than the 
-- due date and with '0' for those were returned on time.
-- Query 1 Solver: 



-- Query 2:
-- Add an extra column ‘LateFee’ to the Library_Branch table, decide late fee per day for each branch and 
-- update that column.
-- Query 2 Solver: 



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
--    • Total Late Fee Balance 'LateFeeBalance' – If the book was not retuned late than fee = ‘0’
-- Query 3 Solver: 


