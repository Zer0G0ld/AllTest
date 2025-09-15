#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main() {
    char *device = "/dev/nvme0n1"; // ajuste conforme o disco
    int fd = open(device, O_RDONLY);
    if (fd < 0) {
        perror("Cannot open device");
        return 1;
    }

    char buffer[512];
    if (read(fd, buffer, sizeof(buffer)) != sizeof(buffer)) {
        perror("Read failed");
        close(fd);
        return 2;
    }

    printf("Storage read OK\n");
    close(fd);
    return 0;
}
