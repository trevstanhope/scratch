### Lists, lists.R
### Trevor Stanhope

## Function definitions.
open.account <- function(total) {
    list(
        deposit = function(amount) { # first subfunction of variable
            if(amount <= 0)
                stop("Deposits must be positive!\n")
            total <<- total + amount
            cat(amount, "deposited. Your balance is", total, "\n\n")
        },
        withdraw = function(amount) { # second subfunction of variable
            if(amount > total)
                stop("You don’t have that much money!\n")
            total <<- total - amount
            cat(amount, "withdrawn. Your balance is", total, "\n\n")
        },
        balance = function() { # third subfunction of variable
            cat("Your balance is", total, "\n\n")
        }
    )
}

# runtime commands
ross <- open.account(100)
robert <- open.account(200)
ross$withdraw(30)
ross$balance()
robert$balance()
ross$deposit(50)
ross$balance()
ross$withdraw(500)

