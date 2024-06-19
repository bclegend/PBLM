-include makefile.include

PYTHON = python3

preprocess:
	$(PYTHON) data_augmentation.py

clean:
	-@$(RM) -r ./preprocess_data