# Pyyne Challenge

Pyyne challenge is a project that consist into a challenge that we have two bank information source and we want to wrap it and expose it to a single controller

## Installation


### VS Code Dev Containers
Install:
- VS Code
  - Dev Containers extension
- Docker

Steps:
- Clone this repository to your local filesystem.
- Press <kbd>F1</kbd> and select the **Dev Containers: Open Folder in Container...** command.
- Select the cloned copy of this folder, wait for the container to start, and try things out!

## Usage Example

```bash
vscode ➜ /workspaces/pyyne (main ✗) $ python3 src/app.py 
Account Balance:
{"accountBalance": 728.0,"currency": "USD"}
Transactions:
[[{"amount"  : 100,"type": "TransactionType.CREDIT","text": "Check deposit"},
  {"amount"  : 25.5,"type": "TransactionType.DEBIT","text": "Debit card purchase"},
  {"amount"  : 225,"type": "TransactionType.DEBIT","text": "Rent payment"}],
 [{"amount"  : 125.0,"type": "TransactionType.DEBIT","text": "Amazon.com"},
  {"amount"  : 500.0,"type": "TransactionType.DEBIT","text": "Car insurance"},
  {"amount"  : 800.0,"type": "TransactionType.CREDIT","text": "Salary"}]]
'----------'
Account Balance Bank 1:
215.5
'USD'
Transactions Bank 1:
[{"amount"  : 100,"type": "1","text": "Check deposit"},
 {"amount"  : 25.5,"type": "2","text": "Debit card purchase"},
 {"amount"  : 225,"type": "2","text": "Rent payment"}]
'----------'
Account Balance Bank 2:
{"accountBalance": 512.5,"currency": "USD"}
Transactions Bank 2:
[{"amount"  : 125.0,"type": "TransactionType.DEBIT","text": "Amazon.com"},
 {"amount"  : 500.0,"type": "TransactionType.DEBIT","text": "Car insurance"},
 {"amount"  : 800.0,"type": "TransactionType.CREDIT","text": "Salary"}]
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
