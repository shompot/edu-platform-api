\# Educational Platform API



An open-source backend for an educational platform aimed at improving access to high-quality educational resources for students/adults in Kyrgyzstan.



The project is currently in active development. The API is being developed as the first step toward the larger educational platform, with the initial focus on building a maintainable backend foundation.



\## Current Status



\*\*Work in Progress\*\*



The current implementation focuses on the backend foundation and user authentication. The API currently supports:



\* User registration

\* User login and credential verification

\* Password hashing

\* Request validation

\* Structured API responses

\* PostgreSQL database integration

\* Automated API and authentication tests



The platform's frontend and educational content are planned for later stages of development.



\## Technology Stack



\* \*\*Python\*\*

\* \*\*FastAPI\*\* — REST API framework

\* \*\*SQLAlchemy\*\* — database ORM

\* \*\*PostgreSQL\*\* — relational database

\* \*\*Pydantic\*\* — request and response validation

\* \*\*Pytest\*\* — automated testing

\* \*\*Passlib / bcrypt\*\* — password hashing

\* \*\*python-dotenv\*\* — environment-based configuration

\* \*\*Git\*\* — version control



\## Project Structure



```text

edu-platform-api/

├── app/

│   ├── db/

│   │   ├── base.py

│   │   └── session.py

│   ├── models/

│   │   ├── \_\_init\_\_.py

│   │   └── user.py

│   ├── routers/

│   │   └── users.py

│   ├── schemas/

│   │   └── user.py

│   ├── services/

│   │   └── security.py

│   └── main.py

├── tests/

│   ├── conftest.py

│   └── test\_users.py

├── .env.example

├── .gitignore

├── LICENSE 

├── README.md

└── requirements.txt

```



\## Architecture



The application is organized into separate layers for API routing, validation schemas, database models, database configuration, and service logic.



\* `routers/` — API endpoints and HTTP-level logic

\* `schemas/` — request and response validation using Pydantic

\* `models/` — SQLAlchemy database models

\* `db/` — database engine, sessions, and declarative base

\* `services/` — reusable application logic such as password hashing

\* `tests/` — automated API and authentication tests



\## Testing



The project uses \*\*Pytest\*\* with FastAPI's `TestClient`.



The test suite currently covers:



\* Password hashing and verification

\* Successful user registration

\* Duplicate user registration

\* Password exclusion from API responses

\* Successful login

\* Invalid credentials

\* Request validation

\* Password length validation



Tests use a separate PostgreSQL test database to keep test data isolated from the development database.



\## Configuration



The application uses environment variables for database configuration.



Create a `.env` file based on `.env.example` and provide the appropriate database connection settings.



\## Running Locally



Clone the repository:



```bash

git clone https://github.com/shompot/edu-platform-api.git

cd edu-platform-api

```



Create and activate a virtual environment:



```bash

python -m venv venv

source venv/bin/activate

```



On Windows:



```bash

venv\\Scripts\\activate

```



Install the dependencies:



```bash

pip install -r requirements.txt

```



Configure the required environment variables using `.env`.



Start the development server:



```bash

uvicorn app.main:app --reload

```



The API will be available at:



`http://127.0.0.1:8000`



FastAPI's interactive API documentation is available at:



`http://127.0.0.1:8000/docs`



\## Running Tests



Make sure the test database is configured through the appropriate environment variable, then run:



```bash

pytest

```



\## Roadmap



The project is currently focused on establishing a solid backend foundation. Planned areas for future development include:



\* Expanding the data model for educational content

\* Developing APIs for educational resources

\* Adding authorization and role-based access control

\* Developing the frontend application

\* Adding educational content and learning features

\* Improving deployment and production infrastructure



\## Motivation



The project was started with the goal of making high-quality educational resources more accessible to high school students in Kyrgyzstan.



The long-term vision is to build an open and community-oriented educational platform, while developing the technical foundation incrementally through an open-source project.



\## License



This project is licensed under the GNU General Public License v3.0 (GPL-3.0). See the \[LICENSE](LICENSE) file for details.

