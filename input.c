int main() {
	int x = 5;
	int y = 3;

	printf("add(%d, %d): %d\n", x, y, add(x,y));	
	printf("sub(%d, %d): %d\n", x, y, sub(x,y));

	return 0;
}

int add(int x, int y) {
	return x + y;
}

int sub(int x, int y) {
	return x - y;
}