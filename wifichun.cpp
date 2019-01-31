/*
 * Copyright (C)2019 - Achmad Chun-Chun Winata Adi <anonychun@gmail.com>
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include <iostream>
#include <fstream>

using namespace std;

// prototipe, deklarasi fungsi
void logo();
int getOption();

// main, program utama
int main() {

	// deklarasi variabel
	int pilihan = getOption();
	char is_continue;

	// enum untuk membuat opsi pilihan angka menjadi kata
	enum option{REPOSITORY = 1, INSTALL, DISCONNECT, FLOODING, RESTART, EXIT = 0};

	// control program
	while (pilihan != EXIT) {

		// control pilihan user
		switch (pilihan) {

			case REPOSITORY: {
				// update dan upgrade repository
				system("clear");
				system("apt update && apt upgrade");
				break;

			} case INSTALL: {
				// install mdk3 dan aircrack-ng
				system("clear");
				system("apt install mdk3 aircrack-ng");
				break;

			} case DISCONNECT: {
				// mengeksekusi file python
				system("clear");
				system("python3 disconnect.py");
				break;

			} case FLOODING: {
				// mengeksekusi file python
				system("clear");
				system("python3 flooding.py");
				break;

			} case RESTART: {
				// mengeksekusi file python
				system("clear");
				system("python3 restart.py");
				break;

			} default: {
				cout << "Pilihan yang anda masukan salah\n" << endl;
				break;
			}

		}

		// label konfirmasi untuk melanjutkan atau memberhentikan program
		label_continue:

		cout << "Lanjutkan? (y/n) : ";
		cin >> is_continue;

		if ((is_continue == 'y') || (is_continue == 'Y')) {
			pilihan = getOption();
		} else if ((is_continue == 'n') || (is_continue == 'N')) {
			break;
		} else {
			goto label_continue;
		}
	}

	// akhir dari program
	cout << "\nProgram Telah Berhenti, Terima Kasih ^_^" << endl;

	cin.get();
	return 0;
}

void logo() {
	cout << "  _   _   _   _   _   _   _   _   _  " << endl;
	cout << " / \\ / \\ / \\ / \\ / \\ / \\ / \\ / \\ / \\ " << endl;
	cout << "( W | i | F | i | - | C | h | u | n )" << endl;
	cout << " \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ " << endl;
	cout << endl;
}

int getOption() {
	int input;
	system("clear");
	logo();
	cout << "Penetration Network !!!" << endl;
	cout << "==============================" << endl;
	cout << "1. Update & Upgrade Repository" << endl;
	cout << "2. Install MDK3 & Aircrack-ng" << endl;
	cout << "3. Disconnect WiFi" << endl;
	cout << "4. Flooding WiFi" << endl;
	cout << "5. Restart Network" << endl;
	cout << "0. Exit" << endl;
	cout << "==============================" << endl;
	cout << "Pilih [1-5]? : ";
	cin >> input;
	return input;
}