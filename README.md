# site_with_db

To projekt strony internetowej, w ktorej testuje konteneryzacje Dockera z wykorzystaniem baz danych oraz logowania w stylu produkcyjnym.

Glownym celem repozytorium jest sprawdzenie, jak aplikacja webowa zachowuje sie w srodowisku zblizonym do realnego wdrozenia: z osobnymi uslugami, izolacja kontenerow, trwaloscia danych i kontrola przeplywu informacji w logach.

W projekcie skupiam sie na:
- uruchamianiu strony i bazy danych w kontenerach Docker,
- testowaniu komunikacji miedzy warstwa frontendowa i backendowa,
- weryfikacji poprawnosci zapisu i odczytu danych,
- sprawdzaniu, jak wyglada logowanie zdarzen aplikacyjnych w warunkach produkcyjnych,
- przygotowaniu podstaw pod dalsza automatyzacje wdrozen i testow.

Repozytorium pelni role srodowiska testowego, w ktorym moge bezpiecznie eksperymentowac z konfiguracja kontenerow, schematami danych i sposobem monitorowania dzialania aplikacji.