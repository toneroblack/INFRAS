username=$(id -u)
if [[ $username -ne o ]]
then
    echo "You do not have root permission, kindly switch to the root account"
    exit 1
fi
aws cloudformation create-stack \
--stack-name $1 \
--parameters file://$2 \
--template-body file://$3 \
--region us-west-2 
