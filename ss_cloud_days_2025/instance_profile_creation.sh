aws bedrock create-inference-profile \
    --inference-profile-name "claude-sonnet-profile" \
    --model-source '{"copyFrom":"arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-sonnet-4-20250514-v1:0"}' \
    --description "Inference profile for Claude Sonnet v2" \
    --client-request-token "token-$(date +%s)”*
