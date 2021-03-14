#include <Arduino.h>
#include <VFS.h>

void test_file(const char *filename)
{
  printf("\n----- TEST FileName: '%s' -----\n", filename);

  char text[64];
  char buff[64];
  int fd;
  sprintf(text, "Hello World ( millis = %d ms )\n", millis());

  fd = open(filename, O_WRONLY | O_CREAT, 0);
  if (fd > -1)
  {
    printf("[open] fd = %d\n", fd);
    printf(">>> %s", text);
    printf("[write] %d bytes\n", write(fd, text, strlen(text)));
    close(fd);
  }
  perror("[perror]");

  fd = open(filename, O_RDONLY, 0);
  if (fd > -1)
  {
    printf("\n[open] fd = %d\n", fd);
    memset(buff, 0, sizeof(buff));
    printf("[read] %d bytes\n<<< %s", read(fd, buff, sizeof(buff)), buff);
    close(fd);
  }
  perror("[perror]");

  FILE *pFile;
  pFile = fopen(filename, "r");
  if (pFile)
  {
    printf("\n[fopen] file = %p\n", pFile);
    memset(buff, 0, sizeof(buff));
    if (fgets(buff, sizeof(buff), pFile) != NULL)
      printf("<<< %s", buff);
    else
      perror("[fgets]");
    fclose(pFile);
  }
  perror("[perror]");

  puts("-------------- END TEST ---------------");
}

void setup()
{
  delay(1000);                // just wait terminal to start
  Serial.begin(115200, true); // retarget stdio
  printf("\n\nArdiuno Raspberrypi PI Pico 2021 Georgi Angelov\n");

#ifdef USE_VFS
  vfs_init(); // mount default
#endif

  test_file("R:/ram_disk.txt");
  test_file("F:/flash_disk.txt");
  test_file("0:/sd_card.txt");

  pinMode(LED, OUTPUT);
}

void loop()
{
  static int led = 0;
  digitalWrite(LED, led);
  led ^= 1;
  delay(500);
  //Serial.printf("%d ", millis());
}

/*

Ardiuno Raspberrypi PI Pico 2021 Georgi Angelov

----- TEST FileName: 'R:/ram_disk.txt' -----
[open] fd = 3
>>> Hello World ( millis = 1012 ms )
[write] 33 bytes
[perror]: Success

[open] fd = 3
[read] 33 bytes
<<< Hello World ( millis = 1012 ms )
[perror]: Success

[fopen] file = 0x200248c4
<<< Hello World ( millis = 1012 ms )
[perror]: Success
-------------- END TEST ---------------

----- TEST FileName: 'F:/flash_disk.txt' -----
[open] fd = 3
>>> Hello World ( millis = 1043 ms )
[write] 33 bytes
[perror]: Success

[open] fd = 3
[read] 33 bytes
<<< Hello World ( millis = 1043 ms )
[perror]: Success

[fopen] file = 0x200248c4
<<< Hello World ( millis = 1043 ms )
[perror]: Success
-------------- END TEST ---------------

----- TEST FileName: '0:/sd_card.txt' -----
[perror]: Not owner
[perror]: Not owner
[perror]: Not owner
-------------- END TEST ---------------

*/