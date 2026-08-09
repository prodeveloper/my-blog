+++
title = 'Write Tests That Read Like a Story'
date = 2026-08-09T09:00:00Z
draft = true
+++

I spent a chunk of this week buried in test code across my repos, and it reminded me of a chapter from Software Engineering at Google that I keep coming back to. The chapter is about test clarity, and the core idea is simple: **a good test should read like a story, not like a method call.**

## Name the behavior, not the method

The easiest win is in the name. A method-oriented test is called `testUpdateBalance`. A behavior-driven test is called `shouldNotAllowWithdrawalsWhenBalanceIsEmpty`. Read that second one out loud with the class name and it becomes a sentence: "BankAccount should not allow withdrawals when balance is empty."

That name is the first thing you see in a failure report. It is your best shot at telling a future engineer what broke before they even open the file. If you need the word "and" in a test name, you are probably testing two behaviors and should split it into two tests.

## Structure every test as given, when, then

Every behavior has three parts: the setup, the action, and the assertion. When you make that structure explicit, the test becomes self-documenting.

```java
@Test
public void transferFundsShouldMoveMoneyBetweenAccounts() {
  // Given two accounts with initial balances of $150 and $20
  Account account1 = newAccountWithBalance(usd(150));
  Account account2 = newAccountWithBalance(usd(20));

  // When transferring $100 from the first to the second account
  bank.transferFunds(account1, account2, usd(100));

  // Then the new account balances should reflect the transfer
  assertThat(account1.getBalance()).isEqualTo(usd(50));
  assertThat(account2.getBalance()).isEqualTo(usd(120));
}
```

The most common violation is merging the "when" and "then" blocks, sprinkling assertions between calls to the system under test. That makes it hard to tell the action apart from the expected result. Keep them separate, and for the vast majority of unit tests you only need one of each.

## Don't put logic in tests

Here is the trap I fall into most often. Test code should be trivially correct on inspection. The moment you add a loop, a conditional, or even a string concatenation, you force the reader to do mental computation instead of just reading the answer off the screen.

The book shows a test that builds a URL with `baseUrl + "/albums"`. It looks fine. Then they inline the whole string and the bug jumps out: `"http://photos.google.com//albums"` with two slashes. One bit of logic hid a real bug. If you feel like you need to write a test to verify your test, something has gone wrong.

## DAMP, not DRY

Production code should be DRY: every concept in one place, no duplication. But tests are different. Tests are meant to be stable, and you want them to break when the system changes. The cost of DRY in tests is that important details get hidden in helper methods full of logic, and the reader has to scroll away to understand what is being tested.

Tests should be DAMP: **Descriptive And Meaningful Phrases**. A little duplication is fine if it makes the test simpler and clearer. I would rather read three explicit lines than chase a chain of helper calls.

## Write failure messages a human can read

A bad failure message says "account is closed." Is that the expected state or the actual one? A good one says "Expected an account in state CLOSED, but got account: {name: my-account, state: OPEN}." The difference is whether you can diagnose the problem from the log alone, without opening the test.

## Remember

The test suite is the documentation your future self actually reads. Name tests after behavior, structure them as given/when/then, keep the logic out, and tolerate a little duplication for clarity. When a test breaks, the name and the failure message should tell you everything you need to know.
