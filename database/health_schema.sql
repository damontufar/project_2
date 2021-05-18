CREATE TABLE "cat_diseases" (
    "id_disease" INT   NOT NULL,
    "disease" VARCHAR   NOT NULL,
    CONSTRAINT "pk_cat_diseases" PRIMARY KEY (
        "id_disease"
     )
);

CREATE TABLE "user_diseases" (
    "id_user_disease" INT   NOT NULL,
    "disease_eval_date" DATE   NOT NULL,
    "id_user" INT   NOT NULL,
    "id_disease" INT   NOT NULL,
    CONSTRAINT "pk_user_diseases" PRIMARY KEY (
        "id_user_disease"
     )
);

CREATE TABLE "cat_habit" (
    "id_habit" INT   NOT NULL,
    "habit" VARCHAR   NOT NULL,
    CONSTRAINT "pk_cat_habit" PRIMARY KEY (
        "id_habit"
     )
);

CREATE TABLE "user_habits" (
    "id_user_habit" INT   NOT NULL,
    "habit_eval_date" DATE   NOT NULL,
    "id_user" INT   NOT NULL,
    "id_habit" INT   NOT NULL,
    "frequency" INT   NOT NULL,
    "unit" VARCHAR   NOT NULL,
    CONSTRAINT "pk_user_habits" PRIMARY KEY (
        "id_user_habit"
     )
);

CREATE TABLE "cat_risks" (
    "id_risks" INT   NOT NULL,
    "combination" INT   NOT NULL,
    "risk" VARCHAR   NOT NULL,
    CONSTRAINT "pk_cat_risks" PRIMARY KEY (
        "id_risks"
     )
);

CREATE TABLE "cat_sex" (
    "id_sex" INT   NOT NULL,
    "name" VARCHAR   NOT NULL,
    CONSTRAINT "pk_cat_sex" PRIMARY KEY (
        "id_sex"
     )
);

CREATE TABLE "user_data" (
    "id_user" INT   NOT NULL,
    "name" VARCHAR   NOT NULL,
    "dob" DATE   NOT NULL,
    "id_sex" INT   NOT NULL,
    "height" INT   NOT NULL,
    "weight" INT   NOT NULL,
    "id_user_habit" INT   NOT NULL,
    "id_user_evaluation" INT   NOT NULL,
    "id_user_disease" INT   NOT NULL,
    CONSTRAINT "pk_user_data" PRIMARY KEY (
        "id_user"
     )
);

CREATE TABLE "user_evaluation" (
    "id_user_evaluation" INT   NOT NULL,
    "evaluation_date" DATE   NOT NULL,
    "id_user" INT   NOT NULL,
    "id_risks" INT   NOT NULL,
    CONSTRAINT "pk_user_evaluation" PRIMARY KEY (
        "id_user_evaluation"
     )
);

ALTER TABLE "user_diseases" ADD CONSTRAINT "fk_user_diseases_id_user" FOREIGN KEY("id_user")
REFERENCES "user_data" ("id_user");

ALTER TABLE "user_diseases" ADD CONSTRAINT "fk_user_diseases_id_disease" FOREIGN KEY("id_disease")
REFERENCES "cat_diseases" ("id_disease");

ALTER TABLE "user_habits" ADD CONSTRAINT "fk_user_habits_id_user" FOREIGN KEY("id_user")
REFERENCES "user_data" ("id_user");

ALTER TABLE "user_habits" ADD CONSTRAINT "fk_user_habits_id_habit" FOREIGN KEY("id_habit")
REFERENCES "cat_habit" ("id_habit");

ALTER TABLE "user_data" ADD CONSTRAINT "fk_user_data_id_sex" FOREIGN KEY("id_sex")
REFERENCES "cat_sex" ("id_sex");

ALTER TABLE "user_data" ADD CONSTRAINT "fk_user_data_id_user_habit" FOREIGN KEY("id_user_habit")
REFERENCES "user_habits" ("id_user_habit");

ALTER TABLE "user_data" ADD CONSTRAINT "fk_user_data_id_user_evaluation" FOREIGN KEY("id_user_evaluation")
REFERENCES "user_evaluation" ("id_user_evaluation");

ALTER TABLE "user_data" ADD CONSTRAINT "fk_user_data_id_user_disease" FOREIGN KEY("id_user_disease")
REFERENCES "user_diseases" ("id_user_disease");

ALTER TABLE "user_evaluation" ADD CONSTRAINT "fk_user_evaluation_id_user" FOREIGN KEY("id_user")
REFERENCES "user_data" ("id_user");

ALTER TABLE "user_evaluation" ADD CONSTRAINT "fk_user_evaluation_id_risks" FOREIGN KEY("id_risks")
REFERENCES "cat_risks" ("id_risks");

