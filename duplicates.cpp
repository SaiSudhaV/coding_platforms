int repeatedNumber(const vector<int> &A) {
    int repeated = A[0], nonRepeated = A[0];
    do{
       repeated = A[repeated];
       nonRepeated = A[A[nonRepeated]];
    }while(nonRepeated != repeated );
    repeated = A[0];
    while(repeated != nonRepeated)
    {
        repeated =A[repeated];
        nonRepeated = A[nonRepeated];
    }
    return repeated;
}