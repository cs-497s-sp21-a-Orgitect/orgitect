# Orgitect

## Purpose

This project is designed to help large organizations coordinate multi-step processes. It aims to provide a reasonably generic platform for defining how different departments (organizational units) should proceed to handle a queue of events that should be processed.

## Applications

There are many different industries that perform tasks which could benefit from the logistical tools of this platform. Some examples include repairs, shipping, college/job applications, onboarding, and citizenship.

## Rationale

We have observed that a lot of large organizations struggle to coordinate when they are divided into many units. Often each department has its own procedures and staff, so performing a task that requires all their cooperation can be taxing. Moreover, administrators usually lack a good way to monitor progress across all departments at once. Therefore, this platform could resolve these issues by providing a structured interface which allows viewing and editing the status of each task.

## Scalability

This idea lends itself well to microservices. Abstract concepts such as "tasks" and "departments" can form the service boundaries of the system, and careful attention to designing the format of communications could allow new services that support additional features to be added seamlessly. 
