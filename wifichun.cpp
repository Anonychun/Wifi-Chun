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

void logo();
int getOption();

int main() {

	int pilihan = getOption();
	char is_continue;

	enum option{DISCONNECT = 1, FLOODING, RESTART, EXIT = 0};

	while (pilihan != EXIT) {

		switch (pilihan) {

			case DISCONNECT: {
				system("clear");
				system("python3 disconnect.py");
				break;

			} case FLOODING: {
				system("clear");
				system("python3 flooding.py");
				break;

			} case RESTART: {
				system("clear");
				system("python3 restart.py");
				break;

			} default: {
				cout << "You entered the wrong choice\n" << endl;
				break;
			}

		}

		label_continue:

		cout << "Continue? (y/n) : ";
		cin >> is_continue;

		if ((is_continue == 'y') || (is_continue == 'Y')) {
			pilihan = getOption();
		} else if ((is_continue == 'n') || (is_continue == 'N')) {
			break;
		} else {
			goto label_continue;
		}
	}

	cout << "\n[+] Quitting" << endl;

	cin.get();
	return 0;
}

void logo() {
	ifstream file;
	string data;

	file.open("logo.txt");
	while (!file.eof()) {
		getline(file, data);
		cout << data << endl;
	} cout << endl;
}

int getOption() {
	int input;
	system("clear");
	logo();
	cout << "https://github.com/Anonychun" << endl;
	cout << "==============================" << endl;
	cout << "1. Disconnect WiFi" << endl;
	cout << "2. Flooding WiFi" << endl;
	cout << "3. Restart Network" << endl;
	cout << "0. Exit" << endl;
	cout << "==============================" << endl;
	cout << "Select [1-3]? : ";
	cin >> input;
	return input;
}
