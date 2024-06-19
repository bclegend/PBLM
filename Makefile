-include makefile.include

PYTHON = python3

install-kit: 
	pip install torch torchvision numpy matplotlib tqdm

preprocess:
	$(PYTHON) data_augmentation.py

clean:
	-@$(RM) -r ./preprocess_data