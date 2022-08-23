Please go this readme.txt document to understand the each artifacts and information to reproduce the project to generate job description

Artifacts:
1. NlpJdGeneratorFE-v1.0.ipynb - Notebook to perform feature engineering activities on given dataset (indeed_job_dataset.csv). It removes duplicaties, replaces null values etc.
2. CompanyCorpusGeneration_v1.0.ipynb - Notebook to extract company information from dataset and creates company corpus
3. SkillsCorpusGenerator-v1.0.ipynb - Notebook to extract skills information from dataset, cleans skills by removing duplicates, spaces, tags, quotes and creates skills corpus corpus
4. RolesResponsibilityCorpusGenerator-v1.0.ipynb - Notebook to extract roles & responsibility information from dataset, cleans roles and responsiblity by removing duplicates, spaces, tags, quotes  and creates roles & responsibility corpus
5. NlpRnnCompanyJdGenerator-v1.0.ipynb - Notebook that generate Company text in the job description by using company corpus
6. NlpRnnRolesAndResponsibilityJdGenerator-v1.0.ipynb - Notebook that generate Roles & Responsiblity text in the job description by using roles & responsibility corpus
7. NlpRnnSkillsJdGenerator-v1.0.ipynb - Notebook that generate Skills text in the job description by using skills corpus
8. NlpLstmJdGenerator-v1.1.ipynb - Notebook that generate Company, Roles & Responsiblity and Skills text in the job description by using company, roles & responsibility and skills corpus
9. NlpGpt2TransformerJdGenerator-v1.2.ipynb - Notebook that generate Company, Roles & Responsiblity and Skills text in the job description by using company, roles & responsibility and skills corpus
10. RNNAccuracy.ipynb - Notebook that performs RNN model accurance measurement using cosine similarity method
11. LSTMAccuracy.ipynb - Notebook that performs LSTM model accurance measurement using cosine similarity method
12. NlpGpt2Accuracy.ipynb - Notebook that performs GPTs Transformer model accurance measurement using cosine similarity method
13. jd_company_corpus_v1.0.csv - Company corpus in csv format
14. jd_company_corpus_v1.0.txt - Company corpus in txt format
15. jd_roles_responsibility_corpus_v1.0.csv - Roles & Responsiblity corpus in csv format
16. jd_roles_responsibility_corpus_v1.0.txt - Roles & Responsiblity corpus in txt format
17. jd_skills_corpus_v1.1.csv - Skills corpus in csv format
18. jd_skills_corpus_v1.1.txt - Skills corpus in txt format
19. lstm_company_model.h5 - LSTM pre-trained model for company corpus
20. lstm_roles_res_model.h5 - LSTM pre-trained model for roles & responsibility corpus
21. ltsm_skills_model.h5 - LSTM pre-trained model for skills corpus
22. rnn_company_model.h5 - RNN pre-trained model for company corpus
23. rnn_roles_res_model.h5 - RNN pre-trained model for roles & responsibility corpus
24. rnn_skills_model.h5 - RNN pre-trained model for skills corpus
25. checkpoint_fine_tuning_run_1.tar - GPT 2 transformer pre-trained model checkpoints data for roles & responsibility corpus
26. checkpoint_fine_tuning_run_2.tar - GPT 2 transformer pre-trained model checkpoints data for skills corpus
27. checkpoint_fine_tuning_run_3.tar - GPT 2 transformer pre-trained model checkpoints data for company corpus
28. dataset description - feature/column description about source dataset
29. indeed_job_dataset.csv - source dataset for job description
30. NlpJdGeneratorAPI-v1.0.ipynb - API notebook code for RNN & LSTM models. This has separate API endpoints for RNN & LSTM models to invoke.
31. main.py  - API notebook code for GPT Transformer models. This has API endpoint for GPT2 Transformer model to invoke.

Procedure to reproduce the project setup:
1. copy indeed_job_dataset.csv dataset into project root folder
2. copy all notebooks in root folder
3. execute NlpJdGeneratorFE-v1.0.ipynb notebook to perform feature engineering tasks
4. execute CompanyCorpusGeneration_v1.ipynb notebook to generate company corpus
5. SkillsCorpusGenerator-v1.0.ipynb notebook to generate skills corpus
6. RolesResponsibilityCorpusGenerator-v1.0.ipynb to generate roles & responsibility corpus
7. copy all pre-trained model data (*.h5) files to root folder
8. execute NlpRnnCompanyJdGenerator-v1.0.ipynb notebook to generate company text for Job description from RNN model
9. execute NlpRnnRolesAndResponsibilityJdGenerator-v1.0.ipynb notebook to generate roles & responsibility text for Job description from RNN model
10. execute NlpRnnSkillsJdGenerator-v1.0.ipynb notebook to generate skills text for Job description from RNN model
11. execute NlpLstmJdGenerator-v1.1.ipynb notebook to generate company, roles & responsibility and skills text for Job description from LSTM model
12. copy checkpoint_fine_tuning_run_1.tar, checkpoint_fine_tuning_run_2.tar and checkpoint_fine_tuning_run_3.tar model data file into root folder
12. execute NlpGpt2TransformerJdGenerator-v1.2.ipynb notebook to generate company, roles & responsibility and skills text for Job description from GPT2 Transformer model
13. execute RNNAccuracy.ipynb notebook to generate accuracy data for RNN model
14. execute LSTMAccuracy.ipynb notebook to generate accuracy data for LSTM model
15. execute NlpGpt2Accuracy.ipynb notebook to generate accuracy data for GPT2 Transformer model
16. NlpJdGeneratorAPI-v1.0.ipynb - deploy RNN & LSTM API on colabCode server and start the server in Google Colab. 
	a. After starts successfully copy the hostname from server console
	b. open browers and access http://<hostname>/api/docs
	c. click on endpont name (ex. POST /api/rnn getRnnJdDescription)
	d. click try me button
	e. paste request object 
	{
		"companyText": "Deloitte",
		"rolesText": "Machine Learning Scientist",
		"skillsText": "Microsoft",
		"nextWords": 100
	}
	f. click on execute button
	g. See API response in response section
	h. stop colabcode server
17. main.py - deploy GPT2 Transformer API on colabCode server and start the server in Google Colab. 
	a. After starts successfully copy the hostname from server console
	b. open browers and access http://<hostname>/api/docs
	c. click on endpont name (ex. POST /api/rnn getRnnJdDescription)
	d. click try me button
	e. paste request object 
	{
		"companyText": "Deloitte",
		"rolesText": "Machine Learning Scientist",
		"skillsText": "Microsoft",
		"nextWords": 100
	}
	f. click on execute button
	g. See API response in response section
	h. stop colabcode server

	
	
	
		