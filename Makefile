start:
	@docker run \
		--name jupyter \
		-d \
		-e JUPYTER_ENABLE_LAB=yes \
		-p 8888:8888 \
		-v $(PWD)/data:/home/jovyan/data \
		-v $(PWD)/notebooks:/home/jovyan/notebooks \
		jupyter/scipy-notebook
	@sleep 1
	@make -s jupyter-list

stop:
	@docker stop jupyter
	@docker rm jupyter

jupyter-list:
	@docker exec -it jupyter jupyter notebook list
