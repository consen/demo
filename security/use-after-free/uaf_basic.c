// https://sensepost.com/blog/2017/linux-heap-exploitation-intro-series-used-and-abused-use-after-free/

#include <malloc.h>
#include <stdio.h>

typedef struct UAFME {
    void (*vulnfunc)();
} UAFME;

void good(){
    printf("I AM GOOD :)\n");
}

void bad(){
    printf("I AM BAD >:|\n");
}

int main(int argc, const char * argv[]){
    printf("[i] Allocating a chunk malloc1 holding a UAFME struct\n");
    UAFME *malloc1 = malloc(sizeof(UAFME));
    malloc1->vulnfunc = good;
    printf("[+] UAFME struct initialized with size: %lu\n", sizeof(UAFME));
    printf("[i] good at %p\n", good);
    printf("[i] bad at %p\n", bad);

    printf("[i] Calling malloc1's vulnfunc: \n");
        malloc1->vulnfunc();

    printf("[i] Freeing malloc1\n");
    free(malloc1);
    printf("[i] Allocating a chunk malloc2 with 24(Assuming 64bit) byte size\n");
    // See why malloc(0) reserves 24+8 bytes in 64bit at: 
    //  https://sensepost.com/blog/2017/painless-intro-to-the-linux-userland-heap/
    long *malloc2 = malloc(0);
    printf("[i] Setting malloc2 to bad's pointer\n");
    *malloc2 = (long)bad;

    printf("[i] Now calling malloc1 vulnfunc again...\n"); 
    // Here is where the use-after-free happens
    // as we are using the free malloc1 which 
    // was populated with a pointer to bad
    printf("[i] malloc1 refs from %p and malloc2 refs from %p\n", &malloc1, &malloc2);
    malloc1->vulnfunc();
}
