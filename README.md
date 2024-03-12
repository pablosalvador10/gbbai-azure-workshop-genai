# Workshop: Taking Generative AI apps to Production with Azure <img src="./utils/images/azure_logo.png" alt="Azure Logo" style="width:30px;height:30px;"/>


Welcome to our workshop focused on advancing generative AI to the production stage. This session is designed to equip you with the necessary tools and frameworks to leverage Azure OpenAI services effectively. Our goal is to provide a comprehensive understanding and hands-on experience with a scalable framework and validation processes aligned with RAG architectures, ensuring your projects are built on solid and efficient foundations.

## 🚀 Workshop Overview
In this workshop, you will learn to build and integrate generative AI applications using Azure OpenAI. We will cover essential topics including:

- **🔄 Scalable Framework Development for Azure OpenAI**: Crafting frameworks that support scalability and robustness for generative AI applications.
- **🔍 Validation Framework** : Implementing validation processes following the RAG (Retrieval-Augmented Generation) architectures to ensure the reliability and accuracy of your AI solutions.
- **🔢 Azure OpenAI Services**: Deep dive into setting up and utilizing Azure's powerful OpenAI services to enhance your generative AI projects.

## 🔧 Prerequisites

Please make sure you have met all the prerequisites for this project. A detailed guide on how to set up your environment and get ready to run all the notebooks and code in this repository can be found in the [SETTINGS.md](SETTINGS.md) file. Please follow the instructions there to ensure a smooth exprience.


## 🔄 Continuous Integration/Continuous Deployment (CI/CD) (preview)

This project leverages GitHub Actions for automating our DevOps lifecycle. More #TODO

You can view the configuration and status of our GitHub Actions workflows in the `.github/workflows` directory and the "Actions" tab of our GitHub repository, respectively.

## 💼 Contributing:

Eager to make significant contributions? Our **[CONTRIBUTING](./CONTRIBUTING.md)** guide is your essential resource! It lays out a clear path.

## 🌲 Project Tree Structure

```markdown
📂 gbbai-azure-ai-template
┣ 📂 notebooks <- For development, EDA, and quick testing (Jupyter notebooks for analysis and development).
┣ 📂 src <- Houses main source code for data processing, feature engineering, modeling, inference, and evaluation.
┣ 📂 test <- Runs unit and integration tests for code validation and QA.
┣ 📂 utils <- Contains utility functions and shared code used throughout the project.
┣ 📜 .env.sample <- Sample environment variables file. Replace with your own.
┣ 📜 .pre-commit-config.yaml <- Config for pre-commit hooks ensuring code quality and consistency.
┣ 📜 01-workshop.ipynb <- Jupyter notebook for the workshop.
┣ 📜 CHANGELOG.md <- Logs project changes, updates, and version history.
┣ 📜 USAGE.md <- Guidelines for using this template.
┣ 📜 environment.yaml <- Conda environment configuration.
┣ 📜 Makefile <- Simplifies common development tasks and commands.
┣ 📜 pyproject.toml <- Configuration file for build system requirements and packaging-related metadata.
┣ 📜 README.md <- Overview, setup instructions, and usage details of the project.
┣ 📜 requirements-codequality.txt <- Requirements for code quality tools and libraries.
┣ 📜 requirements.txt <- General project dependencies.
```
