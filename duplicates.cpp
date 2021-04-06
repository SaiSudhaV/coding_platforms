int duplicate_elementsNumber(const vector<int> &A) {
    int duplicate_elements = A[0], unique_elements = A[0];
    do {
       duplicate_elements = A[duplicate_elements];
       unique_elements = A[A[unique_elements]];
    } while(unique_elements != duplicate_elements );
    duplicate_elements = A[0];
    while(duplicate_elements != unique_elements) {
        duplicate_elements =A[duplicate_elements];
        unique_elements = A[unique_elements];
    }
    return duplicate_elements;
}