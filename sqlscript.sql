-- =============================
-- CLEAN DROP 
-- =============================
DROP TABLE IF EXISTS EventParticipation CASCADE;
DROP TABLE IF EXISTS Event CASCADE;
DROP TABLE IF EXISTS MeetingRoom CASCADE;
DROP TABLE IF EXISTS Fine CASCADE;
DROP TABLE IF EXISTS Loan CASCADE;
DROP TABLE IF EXISTS Copy CASCADE;
DROP TABLE IF EXISTS Book CASCADE;
DROP TABLE IF EXISTS DigitalDevice CASCADE;
DROP TABLE IF EXISTS Asset CASCADE;
DROP TABLE IF EXISTS Member CASCADE;
DROP TABLE IF EXISTS Staff CASCADE;
DROP TABLE IF EXISTS FineRateHistory CASCADE;

-- =============================
-- TABLES
-- =============================

CREATE TABLE Staff (
    StaffID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Position VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    PhoneNumber VARCHAR(20),
    HireDate DATE NOT NULL,
    MentorID INT,
    FOREIGN KEY (MentorID) REFERENCES Staff(StaffID)
);

CREATE TABLE Member (
    MemberID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100) UNIQUE,
    PhoneNumber VARCHAR(20),
    Street VARCHAR(100),
    City VARCHAR(50),
    Zip VARCHAR(10),
    JoinDate DATE,
    IsActive BOOLEAN DEFAULT TRUE
);

CREATE TABLE Asset (
    AssetID INT PRIMARY KEY,
    Title VARCHAR(200),
    ReplacementCost NUMERIC(10,2),
    AssetType VARCHAR(20) CHECK (AssetType IN ('Book','DigitalDevice'))
);

CREATE TABLE Book (
    AssetID INT PRIMARY KEY,
    ISBN VARCHAR(20) UNIQUE,
    PageCount INT CHECK (PageCount > 0),
    Author VARCHAR(100),
    Genre VARCHAR(50),
    Publisher VARCHAR(100),
    PublishYear INT,
    FOREIGN KEY (AssetID) REFERENCES Asset(AssetID)
);

CREATE TABLE DigitalDevice (
    AssetID INT PRIMARY KEY,
    SerialNumber VARCHAR(50) UNIQUE,
    DataCapGB NUMERIC(6,2),
    DeviceType VARCHAR(50),
    Manufacturer VARCHAR(100),
    FOREIGN KEY (AssetID) REFERENCES Asset(AssetID)
);

CREATE TABLE Copy (
    CopyID INT PRIMARY KEY,
    AssetID INT,
    Status VARCHAR(20),
    HomeBranch VARCHAR(100),
    CurrentLocation VARCHAR(100),
    AcquisitionDate DATE,
    FOREIGN KEY (AssetID) REFERENCES Asset(AssetID)
);

CREATE TABLE FineRateHistory (
    RateID INT PRIMARY KEY,
    DailyFineRate NUMERIC(5,2),
    EffectiveFrom DATE,
    EffectiveTo DATE
);

CREATE TABLE Loan (
    LoanID INT PRIMARY KEY,
    MemberID INT,
    CopyID INT,
    StaffID INT,
    CheckoutDate DATE,
    DueDate DATE,
    ReturnDate DATE,
    FineRateAtTime NUMERIC(5,2),
    FOREIGN KEY (MemberID) REFERENCES Member(MemberID),
    FOREIGN KEY (CopyID) REFERENCES Copy(CopyID),
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID)
);

CREATE TABLE Fine (
    FineID INT PRIMARY KEY,
    LoanID INT UNIQUE,
    Amount NUMERIC(10,2),
    PaymentStatus VARCHAR(20) DEFAULT 'Unpaid',
    IssuedDate DATE,
    PaidDate DATE,
    FOREIGN KEY (LoanID) REFERENCES Loan(LoanID)
);

CREATE TABLE MeetingRoom (
    RoomID INT PRIMARY KEY,
    RoomName VARCHAR(50),
    Branch VARCHAR(100),
    Capacity INT
);

CREATE TABLE Event (
    EventID INT PRIMARY KEY,
    EventName VARCHAR(100),
    EventDate DATE,
    StartTime TIME,
    EndTime TIME,
    RoomID INT,
    FOREIGN KEY (RoomID) REFERENCES MeetingRoom(RoomID)
);

CREATE TABLE EventParticipation (
    EventID INT,
    StaffID INT,
    Role VARCHAR(50),
    PRIMARY KEY (EventID, StaffID),
    FOREIGN KEY (EventID) REFERENCES Event(EventID),
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID)
);

-- =============================
-- DATA INSERTS
-- =============================

-- Fine Rate History
INSERT INTO FineRateHistory VALUES (1, 0.50, '2022-01-01', '2022-12-31');
INSERT INTO FineRateHistory VALUES (2, 1.00, '2023-01-01', '2023-12-31');
INSERT INTO FineRateHistory VALUES (3, 1.50, '2024-01-01', NULL);

-- Staff
INSERT INTO Staff VALUES (1, 'Ahmed', 'Hassan', 'Senior Librarian', 'ahmed.hassan@library.eg', '0100000001', '2015-03-10', NULL);
INSERT INTO Staff VALUES (2, 'Mohamed', 'Ali', 'Senior Librarian', 'mohamed.ali@library.eg', '0100000002', '2016-07-20', NULL);
INSERT INTO Staff VALUES (3, 'Omar', 'Khaled', 'Librarian', 'omar.khaled@library.eg', '0100000003', '2018-01-15', 1);
INSERT INTO Staff VALUES (4, 'Youssef', 'Ibrahim', 'Librarian', 'youssef.ibrahim@library.eg', '0100000004', '2019-06-25', 1);
INSERT INTO Staff VALUES (5, 'Mariam', 'Adel', 'Librarian', 'mariam.adel@library.eg', '0100000005', '2020-09-05', 2);

-- Members
INSERT INTO Member VALUES (1, 'Fatma', 'Mahmoud', 'fatma@mail.com', '0111111111', 'Nasr City', 'Cairo', '11511', '2022-01-01', TRUE);
INSERT INTO Member VALUES (2, 'Ali', 'Sayed', 'ali@mail.com', '0111111112', 'Heliopolis', 'Cairo', '11341', '2022-03-10', TRUE);
INSERT INTO Member VALUES (3, 'Hassan', 'Mostafa', 'hassan@mail.com', '0111111113', 'Dokki', 'Giza', '12611', '2022-06-15', TRUE);
INSERT INTO Member VALUES (4, 'Nour', 'Ahmed', 'nour@mail.com', '0111111114', 'Maadi', 'Cairo', '11431', '2023-01-20', TRUE);
INSERT INTO Member VALUES (5, 'Sara', 'Youssef', 'sara@mail.com', '0111111115', 'Zamalek', 'Cairo', '11211', '2023-05-12', TRUE);

-- Assets (Books)
INSERT INTO Asset VALUES (101, 'Alchemist', 150.00, 'Book');
INSERT INTO Asset VALUES (102, 'Atomic Habits', 200.00, 'Book');
INSERT INTO Asset VALUES (103, 'Rich Dad Poor Dad', 180.00, 'Book');

-- Assets (Devices)
INSERT INTO Asset VALUES (201, 'Kindle Paperwhite', 3000.00, 'DigitalDevice');
INSERT INTO Asset VALUES (202, 'iPad Air', 15000.00, 'DigitalDevice');

-- Books
INSERT INTO Book VALUES (101, '9780061122415', 200, 'Paulo Coelho', 'Fiction', 'Harper', 1988);
INSERT INTO Book VALUES (102, '9780735211292', 320, 'James Clear', 'Self-help', 'Penguin', 2018);
INSERT INTO Book VALUES (103, '9781612680194', 250, 'Robert Kiyosaki', 'Finance', 'Plata', 1997);

-- Devices
INSERT INTO DigitalDevice VALUES (201, 'SN001', 8, 'E-Reader', 'Amazon');
INSERT INTO DigitalDevice VALUES (202, 'SN002', 64, 'Tablet', 'Apple');

-- Copies
INSERT INTO Copy VALUES (1001, 101, 'Available', 'Cairo Branch', 'Cairo Branch', '2023-01-01');
INSERT INTO Copy VALUES (1002, 102, 'On Loan', 'Giza Branch', 'On Loan', '2023-02-01');
INSERT INTO Copy VALUES (1003, 201, 'Available', 'Cairo Branch', 'Cairo Branch', '2023-03-01');

-- Loans
INSERT INTO Loan VALUES (1, 1, 1002, 3, '2024-01-01', '2024-01-10', NULL, 1.50);
INSERT INTO Loan VALUES (2, 2, 1001, 4, '2024-01-05', '2024-01-15', '2024-01-20', 1.50);

-- Fine
INSERT INTO Fine VALUES (1, 2, 7.50, 'Paid', '2024-01-20', '2024-01-22');

-- Meeting Rooms
INSERT INTO MeetingRoom VALUES (1, 'Room Nile', 'Cairo Branch', 20);
INSERT INTO MeetingRoom VALUES (2, 'Room Pyramids', 'Giza Branch', 15);

-- Events
INSERT INTO Event VALUES (1, 'Reading Club Cairo', '2024-02-01', '10:00', '12:00', 1);
INSERT INTO Event VALUES (2, 'Kids Story Time', '2024-02-05', '11:00', '12:00', 2);

-- Event Participation
INSERT INTO EventParticipation VALUES (1, 1, 'Organiser');
INSERT INTO EventParticipation VALUES (1, 3, 'Attendee');
INSERT INTO EventParticipation VALUES (2, 2, 'Host');

-- =============================
-- FIXED QUERIES 
-- =============================

-- Active Loans
SELECT
    L.LoanID,
    M.FirstName || ' ' || M.LastName AS MemberName,
    A.Title,
    L.CheckoutDate,
    L.DueDate
FROM Loan L
JOIN Member M ON L.MemberID = M.MemberID
JOIN Copy C ON L.CopyID = C.CopyID
JOIN Asset A ON C.AssetID = A.AssetID
WHERE L.ReturnDate IS NULL;

-- Monthly Summary
SELECT
    TO_CHAR(CheckoutDate, 'YYYY-MM') AS LoanMonth,
    COUNT(*) AS TotalLoans
FROM Loan
GROUP BY LoanMonth;

-- =============================
-- TRIGGER 
-- =============================

CREATE OR REPLACE FUNCTION auto_create_fine_func()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.ReturnDate IS NOT NULL
       AND NEW.ReturnDate > NEW.DueDate
       AND NOT EXISTS (SELECT 1 FROM Fine WHERE LoanID = NEW.LoanID)
    THEN
        INSERT INTO Fine (FineID, LoanID, Amount, PaymentStatus, IssuedDate)
        VALUES (
            (SELECT COALESCE(MAX(FineID), 0) + 1 FROM Fine),
            NEW.LoanID,
            ROUND(
                EXTRACT(DAY FROM (NEW.ReturnDate - NEW.DueDate)) * NEW.FineRateAtTime
            , 2),
            'Unpaid',
            NEW.ReturnDate
        );
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER auto_create_fine
AFTER UPDATE ON Loan
FOR EACH ROW
EXECUTE FUNCTION auto_create_fine_func();
