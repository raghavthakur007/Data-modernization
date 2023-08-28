IDENTIFICATION DIVISION.
PROGRAM-ID. CalculatePremium.
AUTHOR. Udit Sharma.
DATE-WRITTEN. 2023-07-21.
DATE-COMPILED.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 PolicyRecord.
   05 Policy-Number      PIC X(10).
   05 Policy-Holder-Name PIC X(50).
   05 Premium-Amount     PIC 9(9)V99.
   05 Policy-Type        PIC X(15).  // Increased the size to accommodate the longest policy_type
   05 Coverage-Limits    PIC 9(9)V99.
   05 Policy-Premium     PIC 9(9)V99.
   05 Age                PIC 9(3).
   05 Car-Value          PIC 9(9)V99.
   05 Property-Type      PIC X(20).
   05 Property-Value     PIC 9(9)V99.
   05 Coverage-Amount    PIC 9(9)V99.

LINKAGE SECTION.
01 PolicyDB2File.
   05 PolicyDB2Record OCCURS 10 TIMES.
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

PROCEDURE DIVISION USING PolicyDB2File.
    DISPLAY "Calculating premiums for each policy..."
    PERFORM VARYING Record-Count FROM 1 BY 1
      UNTIL Record-Count > 10
      MOVE Policy-Type TO PolicyRecord.Policy-Type
      MOVE Age TO PolicyRecord.Age
      MOVE Car-Value TO PolicyRecord.Car-Value
      MOVE Property-Type TO PolicyRecord.Property-Type
      MOVE Property-Value TO PolicyRecord.Property-Value
      MOVE Coverage-Amount TO PolicyRecord.Coverage-Amount

      IF PolicyRecord.Policy-Type = "CAR_INSURANCE"
          MOVE 100000 TO PolicyRecord.Coverage-Limits
          MOVE 1000 TO PolicyRecord.Policy-Premium

          ADDITIONAL-PREMIUM CAR-INSURANCE
          COMPUTE Policy-Premium(Record-Count) = Policy-Premium(Record-Count) + Premium-Amount-Temp
      ELSE IF PolicyRecord.Policy-Type = "HOME_INSURANCE"
          MOVE 500000 TO PolicyRecord.Coverage-Limits
          MOVE 2000 TO PolicyRecord.Policy-Premium

          ADDITIONAL-PREMIUM HOME-INSURANCE
          COMPUTE Policy-Premium(Record-Count) = Policy-Premium(Record-Count) + Premium-Amount-Temp
      ELSE IF PolicyRecord.Policy-Type = "LIFE_INSURANCE"
          MOVE 1000000 TO PolicyRecord.Coverage-Limits
          MOVE 3000 TO PolicyRecord.Policy-Premium

          ADDITIONAL-PREMIUM LIFE-INSURANCE
          COMPUTE Policy-Premium(Record-Count) = Policy-Premium(Record-Count) + Premium-Amount-Temp
      ELSE
          MOVE 0 TO PolicyRecord.Coverage-Limits
          MOVE 0 TO PolicyRecord.Policy-Premium
      END-IF
      MOVE PolicyRecord.Coverage-Limits TO Coverage-Limits(Record-Count)
      MOVE PolicyRecord.Policy-Premium TO Policy-Premium(Record-Count)
    END-PERFORM.
    DISPLAY "Premiums calculated."
    EXIT PROGRAM.

ADDITIONAL-PREMIUM SECTION.

ADD 300 TO Premium-Amount-Temp  // Additional premium based on age
    IF Age < 25
ADD 200 TO Premium-Amount-Temp
    ELSE IF Age < 41
ADD 100 TO Premium-Amount-Temp
    ELSE IF Age <= 60
ADD 400 TO Premium-Amount-Temp

ADD 0.05 TO Premium-Amount-Temp   // Additional premium based on car value
    IF Car-Value < 20000
ADD 0.08 TO Premium-Amount-Temp
    ELSE IF Car-Value < 50000
ADD 0.10 TO Premium-Amount-Temp

END-ADDITIONAL-PREMIUM.

ADDITIONAL-PREMIUM SECTION.

ADD 300 TO Premium-Amount-Temp  // Additional premium based on age
    IF Age < 25
ADD 200 TO Premium-Amount-Temp
    ELSE IF Age < 41
ADD 100 TO Premium-Amount-Temp
    ELSE IF Age <= 60
ADD 400 TO Premium-Amount-Temp

ADD 0.05 TO Premium-Amount-Temp   // Additional premium based on car value
    IF Car-Value < 20000
ADD 0.08 TO Premium-Amount-Temp
    ELSE IF Car-Value < 50000
ADD 0.10 TO Premium-Amount-Temp

END-ADDITIONAL-PREMIUM.

ADDITIONAL-PREMIUM SECTION.

ADD 300 TO Premium-Amount-Temp  // Additional premium based on age
    IF Age < 25
ADD 200 TO Premium-Amount-Temp
    ELSE IF Age < 41
ADD 100 TO Premium-Amount-Temp
    ELSE IF Age <= 60
ADD 400 TO Premium-Amount-Temp

ADD 0.05 TO Premium-Amount-Temp   // Additional premium based on car value
    IF Car-Value < 20000
ADD 0.08 TO Premium-Amount-Temp
    ELSE IF Car-Value < 50000
ADD 0.10 TO Premium-Amount-Temp

END-ADDITIONAL-PREMIUM.

ADDITIONAL-PREMIUM SECTION.

ADD 300 TO Premium-Amount-Temp  // Additional premium based on age
    IF Age < 25
ADD 200 TO Premium-Amount-Temp
    ELSE IF Age < 41
ADD 100 TO Premium-Amount-Temp
    ELSE IF Age <= 60
ADD 400 TO Premium-Amount-Temp

ADD 0.05 TO Premium-Amount-Temp   // Additional premium based on car value
    IF Car-Value < 20000
ADD 0.08 TO Premium-Amount-Temp
    ELSE IF Car-Value < 50000
ADD 0.10 TO Premium-Amount-Temp

END-ADDITIONAL-PREMIUM.
