CFLAGS = -g -O0

all: test_arm_thumb test_arm test_aarch64 test_ppc

test_ppc: test_ppc.c
	gcc $(CFLAGS) test_ppc.c -lcapstone -lautils -o test_ppc

test_arm: test_arm.c
	gcc $(CFLAGS) test_arm.c -lcapstone -lautils -o test_arm

test_arm_thumb: test_arm_thumb.c
	gcc $(CFLAGS) test_arm_thumb.c -lcapstone -o test_arm_thumb

test_aarch64: test_aarch64.c
	gcc $(CFLAGS) test_aarch64.c -lcapstone -o test_aarch64

clean:
	rm test_arm_thumb test_aarch64 *.o
