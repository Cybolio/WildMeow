# WildMeow – Program Management App

**Developer:** Kim Joshua C. Paltinga  
**App:** Program Management App  
**Tables:** Program, Semester

---

## Setup Instructions

### 1. Install Django
```bash
pip install django
```

### 2. Apply Migrations
```bash
cd wildmeow
python manage.py makemigrations
python manage.py migrate
```

### 3. Run the Development Server
```bash
python manage.py runserver
```

---

## URL Routes

| URL | Description |
|-----|-------------|
| `127.0.0.1:8000/` | Index page — lists all Programs and Semesters |
| `127.0.0.1:8000/program_management/addNewProgram/` | Form to add a new Program |
| `127.0.0.1:8000/program_management/addNewSemester/` | Form to add a new Semester |

---

## Project Structure (Program Management App)

```
wildmeow/
├── manage.py
├── wildmeow/
│   ├── settings.py
│   └── urls.py          ← root URL config (/ → index.html)
└── program_management/
    ├── models.py         ← Program & Semester models
    ├── forms.py          ← ProgramForm & SemesterForm
    ├── views.py          ← index, addNewProgram, addNewSemester
    ├── urls.py           ← app URL patterns
    └── templates/
        └── program_management/
            ├── index.html
            ├── addNewProgram.html
            └── addNewSemester.html
```

---

## Git Branch Workflow

```bash
# Create your branch
git checkout -b kim-program-management

# Stage and commit your work
git add .
git commit -m "feat: add Program Management app with Program and Semester models"

# Push your branch
git push origin kim-program-management
```

Then open a Pull Request to merge into `main` once reviewed.

---

## Instructor Collaborator
Add **tulinjasmine@gmail.com** as a collaborator in:  
`GitHub Repo → Settings → Collaborators → Add people`
