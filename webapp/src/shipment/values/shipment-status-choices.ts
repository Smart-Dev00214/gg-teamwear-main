import { getChoicesFromEnum } from "../../common/util/misc-util";

export enum ShipmentStatusType {
  CREATED = 1,
  CONFIRMED = 2,
  FAILED = 3,
  CANCELLED = 4,
  NOTIFIED = 5,
}

export const ShipmentStatusChoices = getChoicesFromEnum(ShipmentStatusType);
