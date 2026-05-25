#include <stdio.h>
#include <stdlib.h>
#include "cJSON.h"
#include <string.h>

#define MAX_TASKS 100

typedef struct {
    int id;
    char title[256];
    char priority[10];
    int done;
    char created_at[20];
} Task;

void load_tasks(Task *tasks, int *count) {
    FILE *f = fopen("tasks.json", "r");
    if (!f) {
        *count = 0;
        return;
    }

    fseek(f, 0, SEEK_END);
    long size = ftell(f);
    rewind(f);

    char *buffer = malloc(size + 1);
    fread(buffer, 1, size, f);
    buffer[size] = '\0';
    fclose(f);

    cJSON *json = cJSON_Parse(buffer);
    free(buffer);

    *count = cJSON_GetArraySize(json);
    for (int i = 0; i < *count; i++) {
        cJSON *item = cJSON_GetArrayItem(json, i);
        tasks[i].id = cJSON_GetObjectItem(item, "id")->valueint;
        tasks[i].done = cJSON_GetObjectItem(item, "done")->valueint;
        strcpy(tasks[i].title, cJSON_GetObjectItem(item, "title")->valuestring);
        strcpy(tasks[i].priority,   cJSON_GetObjectItem(item, "priority")->valuestring);
        strcpy(tasks[i].created_at, cJSON_GetObjectItem(item, "created_at")->valuestring); 
    }

    cJSON_Delete(json);
}

