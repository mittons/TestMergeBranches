COMMIT_NAME='Q'

mkdir $COMMIT_NAME
echo "commit ${COMMIT_NAME}" > $COMMIT_NAME/README.md
git add .
git commit -m "Commit ${COMMIT_NAME}"
git push origin staging