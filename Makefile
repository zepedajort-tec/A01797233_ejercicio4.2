PYTHON=python3
PIP=pip3

STAT_SCRIPT=app.compute_statistics
CONVERT_SCRIPT=app.convert_numbers
WORD_SCRIPT=app.word_count

STAT_DATA=testing-files/P1/TC1.txt testing-files/P1/TC2.txt testing-files/P1/TC3.txt testing-files/P1/TC4.txt testing-files/P1/TC5.txt testing-files/P1/TC6.txt testing-files/P1/TC7.txt
CONVERT_DATA=testing-files/P2/TC1.txt testing-files/P2/TC2.txt testing-files/P2/TC3.txt testing-files/P2/TC4.txt
WORD_DATA=testing-files/P3/TC1.txt testing-files/P3/TC2.txt testing-files/P3/TC3.txt testing-files/P3/TC4.txt testing-files/P3/TC5.txt

RESULTS=output-files/P1/*.Result-output.txt output-files/P2/*.Result-output.txt output-files/P3/*.Result-output.txt

.PHONY: help install lint run-stat run-convert run-word run-all clean

help:
	@echo "Comandos disponibles:"
	@echo "  make install       -> Install dependencies"
	@echo "  make lint          -> Execute pylint"
	@echo "  make lint-strict   -> Execute strict pylint"
	@echo "  make run-stat      -> Execute Compute Statistics"
	@echo "  make run-convert   -> Execute Converter"
	@echo "  make run-word      -> Execute Word Count"
	@echo "  make run-all       -> Execute all"
	@echo "  make clean         -> Delete output files"

install:
	$(PIP) install -r requirements.txt

lint:
	pylint --exit-zero $(STAT_SCRIPT) $(CONVERT_SCRIPT) $(WORD_SCRIPT)

lint-strict:
	pylint $(STAT_SCRIPT) $(CONVERT_SCRIPT) $(WORD_SCRIPT)

run-stat:
	$(PYTHON) -m $(STAT_SCRIPT) $(STAT_DATA)

run-convert:
	$(PYTHON) -m $(CONVERT_SCRIPT) $(CONVERT_DATA)

run-word:
	$(PYTHON) -m $(WORD_SCRIPT) $(WORD_DATA)

run-all: install lint-strict run-stat run-convert run-word

clean:
	rm -f $(RESULTS)
