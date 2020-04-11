build:
	@docker build -t dna_playground .

start:
	@docker run \
		--name dna_playground \
		-d \
		-p 8888:8888 \
		-v $(PWD)/data:/home/jovyan/data \
		-v $(PWD)/notebooks:/home/jovyan/notebooks \
		dna_playground
	@sleep 1
	@make -s jupyter-list

stop:
	@docker stop dna_playground
	@docker rm dna_playground

jupyter-list:
	@docker exec -it dna_playground jupyter notebook list
