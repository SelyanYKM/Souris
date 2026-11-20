/*
 * Souris.exe - bouge la souris automatiquement (Windows, aucune installation).
 *
 * Double-clic : petit mouvement toutes les 30 secondes.
 * Option      : Souris.exe 10   -> toutes les 10 secondes.
 * Arrêt       : fermer la fenêtre ou Ctrl+C.
 */
#include <windows.h>
#include <stdio.h>
#include <stdlib.h>

static volatile LONG running = 1;

static BOOL WINAPI on_ctrl(DWORD type) {
    (void)type;
    InterlockedExchange(&running, 0);
    return TRUE;
}

static void bouger(int dx) {
    INPUT in = {0};
    in.type = INPUT_MOUSE;
    in.mi.dwFlags = MOUSEEVENTF_MOVE;
    in.mi.dx = dx;
    in.mi.dy = 0;
    SendInput(1, &in, sizeof(INPUT));
}

int main(int argc, char **argv) {
    int intervalle = 30;
    if (argc > 1) {
        int v = atoi(argv[1]);
        if (v > 0) intervalle = v;
    }

    SetConsoleOutputCP(CP_UTF8);
    SetConsoleTitleA("Souris - actif");
    SetConsoleCtrlHandler(on_ctrl, TRUE);

    /* Empêche aussi la mise en veille de l'écran et du PC tant que le programme tourne. */
    SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED);

    printf("Souris active : petit mouvement toutes les %d secondes.\n", intervalle);
    printf("Pour arrêter : fermez cette fenêtre (ou Ctrl+C).\n\n");

    unsigned long nb = 0;
    while (running) {
        bouger(5);
        Sleep(150);
        bouger(-5);
        nb++;

        SYSTEMTIME t;
        GetLocalTime(&t);
        printf("\r[%02d:%02d:%02d] mouvements : %lu   ", t.wHour, t.wMinute, t.wSecond, nb);
        fflush(stdout);

        for (int i = 0; i < intervalle * 10 && running; i++) Sleep(100);
    }

    SetThreadExecutionState(ES_CONTINUOUS);
    printf("\nTerminé.\n");
    return 0;
}
