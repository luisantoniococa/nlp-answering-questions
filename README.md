
# NLP 
#### *by Luis Antonio Coca*

The following is a challenge that I got to develop in 72hrs. Everything from scratch

**Acknowledgments:**
*Thank you for giving me the opportunity to be part of this challenge. It wasn't easy, and I put a lot of time into this repo. I tried other things, but I couldn't get them quite right. Since I couldn't show up empty-handed, I come with a simple API solution in Python. Please review the post-mortem at the end of this readme, where I dig deeper into what could be improved with more time.*

---
### Design choices and coding principles:
Throughout my career in data so far, I've learned that redundancy can help ensure data is passed between functions. I've mostly used functional programming to develop Python packages and functions that can work anywhere. Across my code, I've tried my best to separate parts of the code so that it can be organized and easy to read.

I call this being nice to my future self. I won't remember what I did a month ago. So today, I'm trying my best to be extra clear about what my functions, variables, and typings are. This way, my future self and any colleagues will thank me that we're not spending multiple hours finding out what the code does. This also helps in debugging, since if the function doesn't do what the function name suggests, seeing the logic in the code will be less painful.

### Packaging and deploying code:
I decided to use a script to run my container so that I can pass environment variables like ports if they ever need to be changed in a specific way. The script `run_api.sh` will run from the dockerfile instructions.

Similarly, `run_deployment.sh` takes care of things like building the image, starting Minikube, creating the deployments, and finally using the npl-api-manifest.yaml.

### Testing the code:
Once the API is running, there are a couple of files in the test folder that should be able to be passed with a curl post request. They are direct references to the examples given for this exercise. Here is an example:

`curl -X POST http://localhost:8080/question-answering -H 'Content-Type: multipart/form-data' -F 'file=@example1.txt'`

---
## Post Mortem:
**Things I could have done better:**

*In general, I think I did a good job in tackling and showcasing all the main aspects of dealing with a full task deployment as close as I could get to full production code. That being said, there are many more things that need to be done to make this code ready for deployment.*

*I believe that self-reflection is the best way to grow, not just personally, but also in my career. I took the time to look back at what could have been done better.*

- **Logging:** I realized that I added the logger for the API too late, and if I had implemented it earlier, it would have been a good addition to identify errors and use it for debugging purposes.

- **Diversify models:** While building the pipeline, I experimented with Hugging Face Transformers and spent some time trying to make ONNX work. However, I couldn't get the pipeline quite right. Ideally, I would have found a way to reduce the model weight, store it in something like an AWS S3 bucket, and find a way to import it if the post request called for a different model. However, for this case, I only utilized `distilbert-base-uncased-distilled-squad`.

- **Docker Image size:** I could have spent a little more time managing my Python packages' environments. This could have helped me reduce the overall image size and, in turn, decrease costs (aka storage).

- **Create a custom Python Package for the utils:** Another approach to deal with the tools we have here and made the installation of the requirements.txt inside the container strictly about the API is to create a Python package that deals with the cleaning, sentence, and the question-answering part of the task. This could make reproducibility and version control way easier. Additionally, if anyone on the team wants to use a lighter version of the package that can work with some of the functionalities, they can use them in their own workflow if needed.

- **More robust tests:** As I was getting to the point where I needed to finish, I used a very simple test in Pytest to make sure that the API was running. It worked to a certain degree. However, more traffic tests can be conducted once we can determine how much traffic each endpoint can receive.

- **Volume Scalability:** I would have liked to run a stress test on this cluster and see what their limits are. I know that it depends entirely on the resources given to each container, but experimenting with this could give us a better idea of how the resources are being utilized and how we could optimize them in better ways.

- **NEVER UPDATE WINDOWS TO WINDOWS 11:** I haven't done this type of development on my personal computer in a while, and I had some configurations with my Python environments as well as my Linux subsystem for Windows. All those configurations were lost when I upgraded to Windows 11. It was an unfortunate circumstance that took more time than I wanted to.

### Conclusion

In conclusion, I had a great time working on this challenge and I am happy with what I was able to achieve given the time constraints. This project allowed me to showcase my skills in Python, Docker, and Kubernetes while also giving me an opportunity to reflect on areas where I can improve.

I believe that this project can be further developed to make it more robust and scalable. With the addition of logging, diversifying models, creating a custom python package for the utils, and more robust testing, this project can be made production-ready. Additionally, running stress tests and experimenting with volume scalability can give us a better understanding of how the resources are being utilized and how we can optimize the project further.

Thank you for taking the time to review this project. If you have any questions or feedback, please do not hesitate to reach out to me.

Best,
*Luis Antonio Coca*
