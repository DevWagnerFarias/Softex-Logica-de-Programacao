
int main () {
// declaração do ponteiro
int *ptr
ptr = (int*) malloc (22*sizeof(int))
int ptr [22]

// realocando o ponteiro
ptr = (int*) realloc (ptr, 35*sizeof(int))

//liberando o bloco

free (ptr)

}