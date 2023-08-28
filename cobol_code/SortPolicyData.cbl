IDENTIFICATION DIVISION.
PROGRAM-ID. SortPolicyData.
AUTHOR. Udit Sharma.
DATE-WRITTEN. 2023-07-21.
DATE-COMPILED.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 Temp-Buffer.
   05 Temp-Record OCCURS 10 TIMES.
      10 Policy-Number      PIC X(10).
      10 Policy-Holder-Name PIC X(50).
      10 Premium-Amount     PIC 9(9)V99.
      10 Policy-Type        PIC X(15).  // Increased the size to accommodate the longest policy_type
      10 Coverage-Limits    PIC 9(9)V99.
      10 Policy-Premium     PIC 9(9)V99.
      10 Age                PIC 9(3).
      10 Car-Value          PIC 9(9)V99.
      10 Property-Type      PIC X(20).
      10 Property-Value     PIC 9(9)V99.
      10 Coverage-Amount    PIC 9(9)V99.

PROCEDURE DIVISION USING WS-Sort-Buffer.
    DISPLAY "Sorting policy data using Merge Sort..."
    PERFORM MERGE-SORT(1, 10)  // Assuming 10 records in PolicyDB2Record
    DISPLAY "Policy data sorted."
    EXIT PROGRAM.

MERGE-SORT SECTION.
01 LeftIndex  PIC 9(4) BINARY.
01 RightIndex PIC 9(4) BINARY.
PROCEDURE DIVISION USING LeftIndex, RightIndex.
    IF LeftIndex < RightIndex
        COMPUTE WS-MidPoint = (LeftIndex + RightIndex) / 2
        PERFORM MERGE-SORT(LeftIndex, WS-MidPoint)
        PERFORM MERGE-SORT(WS-MidPoint + 1, RightIndex)
        PERFORM MERGE(LeftIndex, WS-MidPoint, RightIndex)
    END-IF.
    EXIT MERGE-SORT.

MERGE SECTION.
01 WS-MidPoint PIC 9(4) BINARY.
01 I          PIC 9(4) BINARY.
01 J          PIC 9(4) BINARY.
PROCEDURE DIVISION USING LeftIndex, WS-MidPoint, RightIndex.
    MOVE LeftIndex TO I
    MOVE WS-MidPoint + 1 TO J
    MOVE LeftIndex TO K
    PERFORM VARYING M FROM 1 BY 1 UNTIL M > RightIndex - LeftIndex + 1
        IF I > WS-MidPoint
            MOVE PolicyDB2Record(J) TO Temp-Record(M)
            ADD 1 TO J
        ELSE IF J > RightIndex
            MOVE PolicyDB2Record(I) TO Temp-Record(M)
            ADD 1 TO I
        ELSE IF PolicyDB2Record(I).Policy-Number <= PolicyDB2Record(J).Policy-Number
            MOVE PolicyDB2Record(I) TO Temp-Record(M)
            ADD 1 TO I
        ELSE
            MOVE PolicyDB2Record(J) TO Temp-Record(M)
            ADD 1 TO J
        END-IF
    END-PERFORM.
    PERFORM VARYING M FROM 1 BY 1 UNTIL M > RightIndex - LeftIndex + 1
        MOVE Temp-Record(M) TO PolicyDB2Record(K)
        ADD 1 TO K
    END-PERFORM.
    EXIT MERGE.
