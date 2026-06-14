from passlib.context import CryptContext

pass_context = CryptContext(
    schemes=["bcrypt"],
    deprecated = "auto"
)

def hash_password(password: str) -> str:
    return pass_context.hash(password)

def verify_password(plain_pass: str, hashed_pass: str ) -> bool:
    return pass_context.verify(
        plain_pass,
        hashed_pass
    )

