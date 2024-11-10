-- ==========================================================================================================
-- SQL Tables For Part 2
-- ==========================================================================================================

-- PUBLISHER: Publisher_Name, Phone, Address
-- PUBLISHER Table Creator: Chime Nguyen
CREATE TABLE IF NOT EXISTS (
    Publisher_Name VARCHAR(27) NOT NULL, -- The number 27 came from the longest name from the publisher
	Phone CHAR(12) NOT NULL, -- The number 12 came from the max length of the phone number (excluding extensions)
	Address VARCHAR(120) NOT NULL, -- This contains the address of the publisher

	PRIMARY KEY (Publisher_Name), -- Publisher_Name is a primary key that connects PUBLISHER with BOOK
	UNIQUE (Phone) -- Phone is a unique number that corresponds with the Publisher (Secondary Key)
);


-- LIBRARY_BRANCH: Branch_Id, Branch_Name, Branch_Address
-- LIBRARY_BRANCH Table Creator: 



-- BORROWER: Card_No, Name, Address, Phone
-- BORROWER Table Creator: 



-- BOOK: Book_Id, Title, Publisher_name
-- BOOK Table Creator: 



-- BOOK_LOANS: Book_Id, Branch_Id, Card_No, Date_Out, Due_Date, Returned_date
-- BOOK_LOANS Table Creator: 



-- BOOK_COPIES: Book_Id, Branch_Id, No_Of_Copies
-- BOOK_COPIES Table Creator: 



-- BOOK_AUTHORS: Book_Id, Author_Name
-- BOOK_AUTHORS Table Creator: 


