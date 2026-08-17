# Onboarding and pricing snapshot

## Onboarding

1. Register and complete real-name verification.
2. Open the Visual Intelligence console at `https://console.volcengine.com/ai/overview`.
3. Enable the required capability in free-trial or formal mode.
4. Create AK/SK credentials from API access-key management; prefer a least-privilege subaccount where available.
5. Integrate with an official server SDK or Volcengine request signing.
6. Monitor usage, concurrency, errors, latency, renewals, and resource packages in the console.

Never commit AK/SK values to this repository or application source.

## Pricing snapshot

The following values came from pages updated in March–April 2026. The official pages explicitly say the console is authoritative.

### Images

| Capability | Snapshot unit price |
| --- | ---: |
| Image generation 3.0 family | ¥0.20 per successful image/call |
| Image generation 4.0 family | ¥0.22 per generated image |
| Inpainting | ¥0.20 per successful call |
| Intelligent upscaling | ¥0.40 per successful call |
| Image Generation 4.6 | ¥0.22 per generated image |

Free status included a 200-call trial and concurrency 1. Formal concurrency and purchasable expansion varied by capability and console configuration.

### Videos

| Capability | Snapshot unit price | Snapshot formal concurrency |
| --- | ---: | ---: |
| Video Generation 3.0 Pro | ¥1.00/sec | 2 |
| Video Generation 3.0 1080P | ¥0.63/sec | 2 |
| Video Generation 3.0 720P | ¥0.28/sec | 2 |
| Video Generation S2.0 Pro | ¥0.65/sec | 2 |
| Action Imitation | ¥0.50/sec | 1 |
| Digital-human fast mode | ¥1.00/sec | 1 |

Only successfully returned images/videos are documented as billable. Resource packages, discounts, and concurrency purchases are dynamic.

## Billing operations

- Published product prices include VAT unless stated otherwise.
- The tax/invoice page lists a 6% VAT rate for information-technology technical-service fees.
- Unconsumed prepaid balance is not invoiceable; apply against completed orders/bills through the billing center.
- The pages describe a two-hour grace period after account arrears and potential resource release after 24 hours without full payment. Verify current policy before production reliance.
