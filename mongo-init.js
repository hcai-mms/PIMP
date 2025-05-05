db.createUser(
        {
            user: "root",
            pwd: "rootpwd",
            roles: [
                {
                    role: "readWrite",
                    db: "prod"
                }
            ]
        }
);
