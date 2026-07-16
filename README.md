# Personal Expense Tracker

## Project Objective

The Personal Expense Tracker is a command-line application that allows
a user to manage their daily expenses in a simple and structured way.

The user can:
- Add a new expense with an amount, category, date, and description
- List all recorded expenses
- Delete an expense by its ID
- Compute the total spending for a specific category
- Compute the total spending over a given time period

---

## What is Clean Architecture?

Clean Architecture is a software design principle introduced by
Robert C. Martin (Uncle Bob). It organizes code into independent
layers, where each layer has a single responsibility and does not
depend on the layers outside of it.

### The Four Layers

**1. Entities (Domain)**
The core business object. It contains the data and the business
rules that define what a Depense is independent of any database,
framework, or interface. Validation rules such as a strictly positive
amount and a non-empty category are enforced at this level.

**2. Use Cases (Application)**
The actions the application can perform  AddExpense, DeleteExpense,
ListExpenses, ComputeTotalByCategory, ComputeTotalByPeriod. Each use
case represents one specific business operation and depends only on
the repository interface, never on a concrete implementation.

**3. Interface Adapters**
The bridge between the business logic and the outside world. In this
project, two repository implementations are provided: an in-memory
repository for testing purposes and a CSV file repository for
persistent data storage across sessions.

**4. Frameworks & Drivers**
The entry point of the application. It includes the Command Line
Interface (CLI) that receives user input and calls the appropriate
use case, as well as the main.py file that assembles all layers
together through dependency injection.

### Why Clean Architecture?

- Each layer is independent and testable in isolation
- The business logic never depends on the database or the UI
- Swapping the storage backend (memory vs CSV) requires changing a single line
- Easy to maintain, extend, and modify without breaking other layers

---

## Project Structure

```
carnet_depenses/
├── domain/
│   ├── entities/
│   │   └── depense.py
│   └── interfaces/
│       └── i_depense_repository.py
├── usecases/
│   ├── ajouter_depense.py
│   ├── supprimer_depense.py
│   ├── lister_depenses.py
│   ├── calculer_total_categorie.py
│   └── calculer_total_periode.py
├── interface_adapters/
│   ├── repo_memoire.py
│   └── repo_csv.py
├── framework/
│   └── console_app.py
└── main.py
```
